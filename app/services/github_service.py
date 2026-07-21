import httpx

from app.core.config import settings
from app.models.pull_request_models import (
    PullRequestFile,
    PullRequestFilesResponse,
)
from app.utils.github_utils import parse_repository_url


class GitHubService:

    BASE_URL = "https://api.github.com"

    @classmethod
    def get_pull_request_files(
        cls,
        repository_url: str,
        pr_number: int,
    ) -> PullRequestFilesResponse:

        owner, repo = parse_repository_url(repository_url)

        url = (
            f"{cls.BASE_URL}/repos/"
            f"{owner}/{repo}/pulls/{pr_number}/files"
        )

        headers = {
            "Accept": "application/vnd.github+json",
        }

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = (
                f"Bearer {settings.GITHUB_TOKEN}"
            )

        response = httpx.get(
            url,
            headers=headers,
            timeout=30,
        )

        if response.status_code != 200:
            raise Exception(
                f"GitHub API Error "
                f"{response.status_code}\n"
                f"{response.text}"
            )

        data = response.json()

        files = []

        for item in data:

            patch = item.get("patch")

            # Skip files that have no textual diff
            if not patch:
                continue

            files.append(
                PullRequestFile(
                    filename=item.get(
                        "filename",
                        "Unknown File",
                    ),
                    status=item.get(
                        "status",
                        "unknown",
                    ),
                    patch=patch,
                )
            )

        return PullRequestFilesResponse(
            repository=f"{owner}/{repo}",
            pull_request_number=pr_number,
            files=files,
        )