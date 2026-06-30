from pydantic import BaseModel


class ReviewRequest(BaseModel):
    code: str


class ReviewResponse(BaseModel):
    review: str