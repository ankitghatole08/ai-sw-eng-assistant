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
    def get_pull_request_files(cls, repository_url: str, pr_number: int):

        owner, repo = parse_repository_url(repository_url)

        url = f"{cls.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}/files"

        headers = {
            "Accept": "application/vnd.github+json",
        }

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

        response = httpx.get(url, headers=headers, timeout=30)

        if response.status_code != 200:
            raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

        files = []

        for item in response.json():

            raw_url = item.get("raw_url")

            files.append(
                PullRequestFile(
                    filename=item.get("filename", "unknown"),
                    status=item.get("status", "unknown"),
                    raw_url=raw_url,
                    content=None,
                    review=None,
                )
            )

        return PullRequestFilesResponse(
            repository=f"{owner}/{repo}",
            pull_request_number=pr_number,
            files=files,
        )

    @staticmethod
    def fetch_file_content(raw_url: str | None):

        # 🔥 FIX: NEVER CALL HTTP IF NONE
        if not raw_url or not isinstance(raw_url, str):
            return None

        try:
            headers = {}

            if settings.GITHUB_TOKEN:
                headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

            response = httpx.get(raw_url, headers=headers, timeout=30)

            if response.status_code != 200:
                return None

            return response.text

        except Exception:
            return None