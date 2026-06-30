from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.review import router as review_router
from app.api.github import router as github_router

app = FastAPI(
    title="AI Software Engineering Assistant",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(review_router)
app.include_router(github_router)


@app.get("/")
def root():

    return {
        "message": "Welcome to AI Software Engineering Assistant!"
    }