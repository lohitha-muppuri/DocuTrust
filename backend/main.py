from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import shutil
import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI(title="DocuTrust AI")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["docutrust"]
query_logs = db["query_logs"]

# AI Model
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

documents = []
index = None


@app.get("/")
def home():
    return {"status": "DocuTrust Backend Running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global documents, index

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF allowed")

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = PdfReader(path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = []

    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()

        if page_text:
            chunks = splitter.split_text(page_text)

            for chunk in chunks:
                documents.append({
                    "text": chunk,
                    "page": page_num + 1
                })

    if not documents:
        raise HTTPException(status_code=400, detail="Could not read PDF")

    texts = [doc["text"] for doc in documents]

    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks": len(documents)
    }


@app.post("/ask")
async def ask(data: dict):
    global documents, index

    if index is None:
        raise HTTPException(status_code=400, detail="Upload PDF first")

    question = data.get("question")

    if not question:
        raise HTTPException(status_code=400, detail="Question missing")

    q_embedding = model.encode([question])
    q_embedding = np.array(q_embedding).astype("float32")

    distances, ids = index.search(q_embedding, 3)

    best_distance = float(distances[0][0])

    context = ""
    citations = []

    for i in ids[0]:
        if i < len(documents):
            context += documents[i]["text"] + "\n\n"
            citations.append(f"Page {documents[i]['page']}")

    confidence = max(0, min(100, int((1 / (1 + best_distance)) * 100)))
    self_corrected = False

    # CRAG self-correction
    if confidence < 40:
        self_corrected = True

        rewritten_query = question + " detailed explanation"
        q_embedding = model.encode([rewritten_query])
        q_embedding = np.array(q_embedding).astype("float32")

        distances, ids = index.search(q_embedding, 3)

        context = ""
        citations = []

        for i in ids[0]:
            if i < len(documents):
                context += documents[i]["text"] + "\n\n"
                citations.append(f"Page {documents[i]['page']}")

        best_distance = float(distances[0][0])
        confidence = max(0, min(100, int((1 / (1 + best_distance)) * 100)))

    answer = f"""
📄 Relevant Context:

{context}

🤖 AI Response:
Answer generated from retrieved PDF context.
"""

    # Save query logs to MongoDB
    query_logs.insert_one({
        "question": question,
        "confidence": confidence,
        "citations": citations,
        "self_corrected": self_corrected
    })

    return {
        "answer": answer,
        "citations": citations,
        "confidence": confidence,
        "self_corrected": self_corrected
    }