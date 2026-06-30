from fastapi import FastAPI

app = FastAPI(
    title="AI Software Engineering Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Software Engineering Assistant!"
    }