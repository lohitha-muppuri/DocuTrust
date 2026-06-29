class CitationGenerator:

    def generate(self, chunks):

        citations = []

        for chunk in chunks:

            meta = chunk["metadata"]

            citations.append({

                "document": meta["document"],

                "page": meta["page"],

                "chunk_id": meta["chunk_id"],

                "score": round(

                    chunk.get(

                        "relevance_score",

                        chunk.get(

                            "score",

                            0

                        )

                    ),

                    4

                )

            })

        return citations


citation_generator = CitationGenerator()