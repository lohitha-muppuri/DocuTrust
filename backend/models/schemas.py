from typing import List, Optional
from pydantic import BaseModel, Field


# -----------------------------
# Upload Models
# -----------------------------

class UploadResponse(BaseModel):
    message: str
    filename: str
    path: str


# -----------------------------
# Chat Request
# -----------------------------

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)


# -----------------------------
# Citation Model
# -----------------------------

class Citation(BaseModel):
    document: str
    page: int
    chunk_id: int
    score: float


# -----------------------------
# Chat Response
# -----------------------------

class ChatResponse(BaseModel):
    question: str
    answer: str
    confidence: float
    citations: List[Citation]


# -----------------------------
# Document Metadata
# -----------------------------

class DocumentMetadata(BaseModel):
    filename: str
    page: int
    chunk_id: int
    text: str


# -----------------------------
# Retrieved Chunk
# -----------------------------

class RetrievedChunk(BaseModel):
    score: float
    metadata: DocumentMetadata


# -----------------------------
# Workflow Log
# -----------------------------

class WorkflowLog(BaseModel):
    step: str
    status: str
    message: str


# -----------------------------
# Query Rewrite
# -----------------------------

class RewriteResponse(BaseModel):
    original_query: str
    rewritten_query: str


# -----------------------------
# Confidence
# -----------------------------

class ConfidenceResponse(BaseModel):
    confidence: float
    reason: str


# -----------------------------
# Search Response
# -----------------------------

class SearchResponse(BaseModel):
    chunks: List[RetrievedChunk]