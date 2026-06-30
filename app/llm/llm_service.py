from app.llm.gemini_provider import GeminiProvider


class LLMService:

    def __init__(self):

        self.provider = GeminiProvider()

    def review_code(
        self,
        code: str,
    ) -> str:

        return self.provider.generate_review(code)