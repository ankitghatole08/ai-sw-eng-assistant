from github import Github
from github.GithubException import GithubException

from app.models.github_models import (
    GitHubFileRequest,
    GitHubFileResponse,
)


class GitHubService:

    @staticmethod
    def get_file(
        request: GitHubFileRequest,
    ) -> GitHubFileResponse:

        try:

            github = Github()

            repository = github.get_repo(
                f"{request.owner}/{request.repository}"
            )

            file = repository.get_contents(
                request.file_path
            )

            return GitHubFileResponse(
                file_name=file.name,
                content=file.decoded_content.decode("utf-8")
            )

        except GithubException as error:

            raise Exception(
                f"GitHub Error: {error.data}"
            )