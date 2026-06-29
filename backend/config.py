from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

DATABASE_NAME = os.getenv("DATABASE_NAME")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

FAISS_PATH = os.getenv("FAISS_PATH")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

CROSS_ENCODER_MODEL = os.getenv("CROSS_ENCODER_MODEL")

LLM_MODEL = os.getenv("LLM_MODEL")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))