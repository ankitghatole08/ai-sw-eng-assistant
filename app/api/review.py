from fastapi import APIRouter

from app.models.review_models import (
    ReviewRequest,
    ReviewResponse,
)

from app.services.review_service import (
    ReviewService,
)

router = APIRouter(
    prefix="/review",
    tags=["AI Review"],
)


@router.post(
    "/",
    response_model=ReviewResponse,
)
def review_code(
    request: ReviewRequest,
):

    return ReviewService.review_code(request)