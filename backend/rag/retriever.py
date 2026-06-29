from backend.embeddings.embedding import embedding_model
from backend.embeddings.vectorstore import vector_store


class Retriever:

    def __init__(self):

        if vector_store.index is None:
            vector_store.load()

    def retrieve(self, question, top_k=5):

        query_embedding = embedding_model.embed_query(question)

        results = vector_store.similarity_search(
            query_embedding,
            top_k
        )

        return results


retriever = Retriever()