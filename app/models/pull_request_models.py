from pydantic import BaseModel, HttpUrl


class PullRequestReviewRequest(BaseModel):
    repository_url: HttpUrl
    pull_request_number: int


class PullRequestFile(BaseModel):
    filename: str
    status: str
    raw_url: str | None = None
    content: str | None = None
    review: str | None = None


class PullRequestFilesResponse(BaseModel):
    repository: str
    pull_request_number: int
    files: list[PullRequestFile]


class PullRequestReviewResponse(BaseModel):
    repository: str
    pull_request_number: int
    overall_score: int
    summary: str
    files: list[PullRequestFile]