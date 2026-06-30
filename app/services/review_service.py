from app.llm.llm_service import LLMService
from app.models.review_models import (
    ReviewRequest,
    ReviewResponse,
)


class ReviewService:

    @staticmethod
    def review_code(
        request: ReviewRequest,
    ) -> ReviewResponse:

        llm = LLMService()

        review = llm.review_code(
            request.code
        )

        return ReviewResponse(
            review=review
        )