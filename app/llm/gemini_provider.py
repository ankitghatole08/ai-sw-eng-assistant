from google import genai
from google.genai import types

from app.core.config import settings
from app.llm.base import BaseLLMProvider


class GeminiProvider(BaseLLMProvider):

    def __init__(self):

        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_review(
        self,
        code: str,
    ) -> str:

        prompt = f"""
You are a Senior Software Engineer performing a professional code review.

Review the following code.

Provide:

1. Overall assessment
2. Code quality issues
3. Bugs
4. Best practice suggestions
5. Security concerns (if any)

Code:

{code}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            ),
        )

        return response.text