from app.models.pull_request_models import (
    PullRequestReviewResponse,
)

from app.services.ai_review_service import (
    AIReviewService,
)

from app.services.github_service import (
    GitHubService,
)


class ReviewService:

    def __init__(self):

        self.ai = AIReviewService()

    def review_pull_request(
        self,
        repository_url: str,
        pull_request_number: int,
    ):

        pr = GitHubService.get_pull_request_files(
            repository_url,
            pull_request_number,
        )

        reviewed_files = []

        score = 0

        reviewed = 0

        for file in pr.files:

            if not file.patch:

                file.review = (
                    "Skipped (No Git diff available)"
                )

                reviewed_files.append(file)

                continue

            try:

                review = self.ai.review_patch(
                    file.filename,
                    file.patch,
                )

                file.review = review

                score += 8

                reviewed += 1

            except Exception as e:

                file.review = (
                    f"AI Review Failed:\n\n{str(e)}"
                )

            reviewed_files.append(file)

        overall = (
            int(score / reviewed)
            if reviewed
            else 0
        )

        return PullRequestReviewResponse(
            repository=pr.repository,
            pull_request_number=pull_request_number,
            overall_score=overall,
            summary=(
                f"Reviewed "
                f"{reviewed} "
                f"changed files."
            ),
            files=reviewed_files,
        )