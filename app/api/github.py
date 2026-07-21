from fastapi import APIRouter, HTTPException

from app.models.github_models import (
    GitHubFileRequest,
    GitHubFileResponse,
    GitHubReviewResponse,
)

from app.services.github_service import (
    GitHubService,
)

from app.services.review_service import (
    ReviewService,
)

router = APIRouter(
    prefix="/github",
    tags=["GitHub"],
)


@router.post(
    "/file",
    response_model=GitHubFileResponse,
)
def get_file(
    request: GitHubFileRequest,
):

    try:

        return GitHubService.get_file(
            request
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.post(
    "/review",
    response_model=GitHubReviewResponse,
)
def review_github_file(
    request: GitHubFileRequest,
):

    try:

        return ReviewService.review_github_file(
            request
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )