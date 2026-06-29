from sentence_transformers import CrossEncoder

from backend.config import CROSS_ENCODER_MODEL


class RelevanceGrader:

    def __init__(self):

        self.model = CrossEncoder(
            CROSS_ENCODER_MODEL
        )

    def grade(self, question, retrieved_chunks):

        pairs = []

        for chunk in retrieved_chunks:

            pairs.append(

                [

                    question,

                    chunk["metadata"]["text"]

                ]

            )

        scores = self.model.predict(pairs)

        graded_results = []

        for score, chunk in zip(scores, retrieved_chunks):

            chunk["relevance_score"] = float(score)

            graded_results.append(chunk)

        graded_results.sort(

            key=lambda x: x["relevance_score"],

            reverse=True

        )

        return graded_results

    def is_good_retrieval(

        self,

        graded_chunks,

        threshold=0.60

    ):

        if len(graded_chunks) == 0:

            return False

        average = sum(

            c["relevance_score"]

            for c in graded_chunks

        ) / len(graded_chunks)

        return average >= threshold


grader = RelevanceGrader()