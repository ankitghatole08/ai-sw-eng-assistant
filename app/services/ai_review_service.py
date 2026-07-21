from app.llm.llm_service import LLMService


class AIReviewService:

    def __init__(self):
        self.llm = LLMService()

    def review_code(self, code: str) -> str:

        prompt = f"""
You are a senior software engineer.

Perform a detailed code review.

Return:
- Issues
- Improvements
- Security risks
- Best practices
- Short summary

Code:
{code}
"""

        return self.llm.review_code(prompt)