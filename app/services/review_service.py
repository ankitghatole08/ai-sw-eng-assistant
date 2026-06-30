from app.models.review_models import (
    ReviewRequest,
    ReviewResponse,
)


class ReviewService:

    @staticmethod
    def review_code(
        request: ReviewRequest
    ) -> ReviewResponse:

        code = request.code.lower()

        if "print" in code:

            review = (
                "Code looks good.\n\n"
                "Suggestion:\n"
                "- Consider replacing print() with the logging module in production applications."
            )

        else:

            review = (
                "Code received successfully.\n\n"
                "AI review will be available once Gemini is integrated."
            )

        return ReviewResponse(review=review)