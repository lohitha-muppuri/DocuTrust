from transformers import pipeline

from backend.config import LLM_MODEL


class AnswerGenerator:

    def __init__(self):

        self.generator = pipeline(

            "text-generation",

            model=LLM_MODEL

        )

    def generate(

            self,

            question,

            chunks

    ):

        context = ""

        for chunk in chunks:

            context += chunk["metadata"]["text"] + "\n"

        prompt = f"""

Answer ONLY using the following context.

Context:

{context}

Question:

{question}

Answer:

"""

        response = self.generator(

            prompt,

            max_new_tokens=250,

            do_sample=False

        )

        return response[0]["generated_text"]


generator = AnswerGenerator()