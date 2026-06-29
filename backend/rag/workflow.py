from backend.rag.retriever import retriever
from backend.rag.grader import grader
from backend.rag.rewriter import rewriter
from backend.rag.generator import generator
from backend.rag.citations import citation_generator
from backend.rag.confidence import confidence_calculator


class CRAGWorkflow:

    def run(self, question):

        retrieved = retriever.retrieve(question)

        graded = grader.grade(

            question,

            retrieved

        )

        if not grader.is_good_retrieval(graded):

            new_query = rewriter.rewrite(question)

            retrieved = retriever.retrieve(new_query)

            graded = grader.grade(

                new_query,

                retrieved

            )

            question = new_query

        answer = generator.generate(

            question,

            graded

        )

        citations = citation_generator.generate(

            graded

        )

        confidence = confidence_calculator.calculate(

            graded

        )

        return {

            "question": question,

            "answer": answer,

            "confidence": confidence,

            "citations": citations

        }


workflow = CRAGWorkflow()