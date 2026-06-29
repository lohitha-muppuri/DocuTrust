# DocuTrust AI
Enterprise Advanced RAG Platform with Automated Self-Correction

DocuTrust AI is a Retrieval-Augmented Generation (RAG) based system that allows users to upload PDFs and ask questions with citation-backed, confidence-scored answers using an intelligent self-correction pipeline (CRAG).

🚀 Features
📄 PDF upload and processing
🔍 Semantic chunk-based retrieval
🧠 RAG pipeline using embeddings + vector search
🔄 Self-correction (CRAG) for low confidence answers
📊 Confidence scoring system
📌 Page-level citations
🗄 Query logging system
⚡ FastAPI backend
🏗 Architecture

PDF Upload
→ Text Extraction
→ Chunking
→ Embedding Generation
→ Vector Storage (FAISS / DB)
→ Semantic Retrieval
→ Confidence Scoring
→ Self-Correction (if needed)
→ Final Answer with Citations

💻 Tech Stack
Frontend
HTML
CSS
JavaScript
PDF.js
Backend
FastAPI
Python
FAISS
Sentence Transformers
MongoDB
PyPDF
📂 Project Structure
DocuTrust-AI/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── model/
│   ├── parser/
│   ├── rag/
│   ├── utils/
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── README.md
└── ENV_SETUP.txt
⚙️ Setup Instructions
1️⃣ Create Virtual Environment
python -m venv venv

✅ venv is built into Python (no extra installation required)

2️⃣ Activate Virtual Environment
🪟 Windows (CMD / PowerShell)
venv\Scripts\activate

If PowerShell blocks activation:

Set-ExecutionPolicy Unrestricted -Scope Process
venv\Scripts\activate
🍎 Mac / Linux
source venv/bin/activate
✅ Confirm Activation

After activation, you should see:

(venv) C:\your-project>

This means all dependencies will install inside the virtual environment.

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Backend Server
python -m uvicorn main:app --reload

Backend will run at:

http://127.0.0.1:8000
5️⃣ Run Frontend
Option 1 (Direct)

Open:

frontend/index.html
Option 2 (Recommended)
python -m http.server 5500

Then open:

http://localhost:5500
🔄 Daily Workflow (Important)

Every time you reopen the project:

# Step 1: Activate venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Step 2: Run backend
python -m uvicorn main:app --reload
🔐 Environment Variables

Create a .env file and configure:

OPENAI_API_KEY=your_key_here
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
🎯 Problem Statement

Traditional document QA systems suffer from:

Hallucinated answers
Weak retrieval quality
Missing citations

DocuTrust solves this using:

RAG pipeline
Confidence scoring
Self-correction system
Strict citation enforcement
🔮 Future Enhancements
OCR support for scanned PDFs
Multi-document search
Role-based access control
Cloud deployment
LLM fine-tuning
👩‍💻 Author

Developed by Lohitha Muppuri
