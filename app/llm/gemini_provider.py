from google import genai
from google.genai import types

from app.core.config import settings
from app.llm.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        if not settings.GEMINI_API_KEY:

            raise ValueError(
                "Gemini API Key missing."
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_review(
        self,
        prompt: str,
    ) -> str:

        # Gemini performs much better on shorter prompts.
        # Protect against extremely large PRs.
        if len(prompt) > 15000:

            prompt = prompt[:15000]

            prompt += (
                "\n\n"
                "[Diff truncated due to length.]"
            )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            ),
        )

        if (
            response is None
            or not getattr(response, "text", None)
        ):

            return (
                "Gemini returned an empty response."
            )

        return response.text