"""the main module"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import APIRouter, FastAPI

from app.api.messages import router as messages_router
from app.database.connect import client


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = client
    yield
    await app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(messages_router)

app.include_router(api_router)


if __name__ == "__main__":
    # uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run("main:app", reload=True)
