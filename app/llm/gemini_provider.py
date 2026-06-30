from app.llm.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def generate_review(
        self,
        code: str,
    ) -> str:

        return (
            "Gemini provider is configured correctly.\n\n"
            "Real AI responses will be added in the next phase."
        )