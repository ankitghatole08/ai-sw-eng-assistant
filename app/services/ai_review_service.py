from app.llm.llm_service import LLMService


class AIReviewService:

    def __init__(self):
        self.llm = LLMService()

    def review_patch(
        self,
        filename: str,
        patch: str,
    ) -> str:

        prompt = f"""
You are a Senior Software Engineer.

You are reviewing a GitHub Pull Request.

The following text is a Git diff (NOT the entire file).

Review ONLY the changes.

Provide your response in Markdown.

Include:

## Summary

## Potential Bugs

## Code Quality

## Best Practices

## Security Concerns

## Final Recommendation

File:
{filename}

Git Diff:

{patch}
"""

        return self.llm.review_code(prompt)