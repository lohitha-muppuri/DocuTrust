from sentence_transformers import SentenceTransformer

from backend.config import EMBEDDING_MODEL


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed_documents(self, texts):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings

    def embed_query(self, query):

        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embedding


embedding_model = EmbeddingModel()