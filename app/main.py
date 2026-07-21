from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
import sys

from app.api.review import router as review_router

app = FastAPI()

app.include_router(review_router)


# 🔥 HARD DEBUG MIDDLEWARE (CATCH EVERYTHING)
@app.middleware("http")
async def debug_middleware(request: Request, call_next):

    try:
        response = await call_next(request)
        return response

    except Exception as e:

        print("\n🔥🔥🔥 BACKEND CRASH DETECTED 🔥🔥🔥")
        traceback.print_exc(file=sys.stdout)

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "type": type(e).__name__
            }
        )


@app.get("/")
def root():
    return {"status": "OK"}