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
        prompt: str,
    ) -> str:

        # Protect against very large pull requests
        if len(prompt) > 15000:

            prompt = prompt[:15000]

            prompt += (
                "\n\n"
                "[Git diff truncated because it exceeded the maximum prompt length.]"
            )

        try:

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
                    "⚠️ Gemini returned an empty response.\n\n"
                    "Please try again later."
                )

            return response.text

        except Exception as e:

            error = str(e)

            # Free tier quota exceeded
            if (
                "RESOURCE_EXHAUSTED" in error
                or "429" in error
                or "quota" in error.lower()
            ):
                return (
                    "⚠️ **Gemini API quota reached**\n\n"
                    "The AI review could not be generated because the free-tier "
                    "Gemini API request limit has been reached.\n\n"
                    "**What you can do:**\n"
                    "- Wait for the quota to reset.\n"
                    "- Use another Gemini API key.\n"
                    "- Upgrade your Gemini API plan.\n\n"
                    "✅ GitHub Pull Request analysis completed successfully."
                )

            # Timeout
            if "timeout" in error.lower():
                return (
                    "⚠️ The request to Gemini timed out.\n\n"
                    "Please try again in a few moments."
                )

            # Connection issues
            if (
                "connection" in error.lower()
                or "network" in error.lower()
            ):
                return (
                    "⚠️ Unable to connect to the Gemini API.\n\n"
                    "Please check your internet connection and try again."
                )

            # Fallback
            return (
                "⚠️ An unexpected error occurred while generating the AI review.\n\n"
                f"Details:\n{error}"
            )