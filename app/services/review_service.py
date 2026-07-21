from app.services.github_service import GitHubService
from app.services.ai_review_service import AIReviewService
from app.models.pull_request_models import PullRequestReviewResponse


class ReviewService:

    def __init__(self):
        self.ai = AIReviewService()

    def review_pull_request(self, repository_url: str, pull_request_number: int):

        pr_data = GitHubService.get_pull_request_files(
            repository_url,
            pull_request_number,
        )

        reviewed_files = []
        total_score = 0
        reviewed_count = 0

        for file in pr_data.files:

            try:
                content = GitHubService.fetch_file_content(file.raw_url)
                file.content = content

                # 🔥 HARD GUARD (this fixes your Flask crash)
                if not content or not isinstance(content, str):
                    file.review = "Skipped: No readable content"
                    reviewed_files.append(file)
                    continue

                # 🔥 AI SAFETY WRAP
                try:
                    review = self.ai.review_code(content)
                except Exception as e:
                    review = f"AI error: {str(e)}"

                file.review = review

                score = self._score(content, review)

                total_score += score
                reviewed_count += 1

            except Exception as e:
                file.review = f"Processing error: {str(e)}"

            reviewed_files.append(file)

        overall_score = (
            int(total_score / reviewed_count)
            if reviewed_count > 0
            else 0
        )

        summary = (
            f"Reviewed {reviewed_count} files successfully."
            if reviewed_count > 0
            else "No reviewable files found (likely missing raw content from GitHub API)."
        )

        return PullRequestReviewResponse(
            repository=pr_data.repository,
            pull_request_number=pull_request_number,
            overall_score=overall_score,
            summary=summary,
            files=reviewed_files,
        )

    def _score(self, content: str, review: str) -> int:
        score = 7

        if len(content) < 50:
            score -= 1

        if review and "security" in review.lower():
            score -= 2

        if review and "good" in review.lower():
            score += 1

        return max(1, min(score, 10))