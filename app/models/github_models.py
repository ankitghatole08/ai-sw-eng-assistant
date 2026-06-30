from pydantic import BaseModel


class GitHubFileRequest(BaseModel):
    owner: str
    repository: str
    file_path: str


class GitHubFileResponse(BaseModel):
    file_name: str
    content: str