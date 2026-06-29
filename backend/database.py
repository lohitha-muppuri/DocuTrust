from pymongo import MongoClient

from backend.config import MONGODB_URI
from backend.config import DATABASE_NAME

client = MongoClient(MONGODB_URI)

db = client[DATABASE_NAME]

users_collection = db["users"]

documents_collection = db["documents"]

chat_collection = db["chat_logs"]

workflow_collection = db["workflow_logs"]