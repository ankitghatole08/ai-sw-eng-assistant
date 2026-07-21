from fastapi import APIRouter, HTTPException

from app.models.pull_request_models import PullRequestReviewRequest
from app.services.review_service import ReviewService

router = APIRouter(
    prefix="/review",
    tags=["AI Review"],
)


@router.post("/pull-request")
def review_pull_request(request: PullRequestReviewRequest):

    try:

        service = ReviewService()

        return service.review_pull_request(
            repository_url=str(request.repository_url),
            pull_request_number=request.pull_request_number,
        )

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))