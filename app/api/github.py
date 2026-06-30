from fastapi import APIRouter, HTTPException

from app.models.github_models import (
    GitHubFileRequest,
    GitHubFileResponse,
)

from app.services.github_service import (
    GitHubService,
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