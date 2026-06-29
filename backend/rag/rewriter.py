from transformers import pipeline


class QueryRewriter:

    def __init__(self):

        self.rewriter = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    def rewrite(self, query):

        prompt = f"Rewrite this search query to improve document retrieval:\n{query}"

        result = self.rewriter(
            prompt,
            max_new_tokens=50
        )

        return result[0]["generated_text"]


rewriter = QueryRewriter()