class ConfidenceCalculator:

    def calculate(self, graded_chunks):

        if len(graded_chunks) == 0:

            return 0.0

        scores = [

            chunk["relevance_score"]

            for chunk in graded_chunks

        ]

        confidence = sum(scores) / len(scores)

        confidence = max(

            0,

            min(

                confidence,

                1

            )

        )

        return round(

            confidence * 100,

            2

        )


confidence_calculator = ConfidenceCalculator()