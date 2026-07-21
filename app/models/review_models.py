from pydantic import BaseModel, HttpUrl


class ReviewRequest(BaseModel):
    code: str


class ReviewResponse(BaseModel):
    review: str


class PullRequestReviewRequest(BaseModel):
    repository_url: HttpUrl
    pull_request_number: int


class FileReview(BaseModel):
    file_name: str
    review: str


class PullRequestReviewResponse(BaseModel):
    summary: str
    overall_score: int
    files: list[FileReview]