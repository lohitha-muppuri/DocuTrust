import os
import pickle

import faiss
import numpy as np

from backend.config import FAISS_PATH

os.makedirs(FAISS_PATH, exist_ok=True)


class VectorStore:

    def __init__(self):

        self.index = None

        self.metadata = []

        self.dimension = None

    def create_index(self, embeddings):

        self.dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(self.dimension)

        self.index.add(embeddings.astype("float32"))

    def add_documents(self, embeddings, metadata):

        if self.index is None:

            self.create_index(embeddings)

        else:

            self.index.add(embeddings.astype("float32"))

        self.metadata.extend(metadata)

    def save(self):

        faiss.write_index(

            self.index,

            os.path.join(

                FAISS_PATH,

                "index.faiss"

            )

        )

        with open(

            os.path.join(

                FAISS_PATH,

                "metadata.pkl"

            ),

            "wb"

        ) as file:

            pickle.dump(

                self.metadata,

                file

            )

    def load(self):

        index_path = os.path.join(

            FAISS_PATH,

            "index.faiss"

        )

        metadata_path = os.path.join(

            FAISS_PATH,

            "metadata.pkl"

        )

        if not os.path.exists(index_path):

            return False

        self.index = faiss.read_index(index_path)

        with open(metadata_path, "rb") as file:

            self.metadata = pickle.load(file)

        self.dimension = self.index.d

        return True

    def similarity_search(self, query_embedding, top_k=5):

        if self.index is None:

            raise Exception("Vector index not found.")

        scores, indices = self.index.search(

            np.array(

                [query_embedding],

                dtype="float32"

            ),

            top_k

        )

        results = []

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:

                continue

            results.append({

                "score": float(score),

                "metadata": self.metadata[idx]

            })

        return results


vector_store = VectorStore()