"""Users routs processing module."""

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from app.database.database import add_message, retrieve_messages
from app.schemes.messages import (
    AddMessageSchema,
    ListMessageSchema,
    MessageSchema
)

router = APIRouter(prefix="/messages", tags=["messages"])


@router.get(
    path="/",
    response_model=ListMessageSchema,
    status_code=200,
)
@cache(expire=60 * 10, namespace="fastapi_get_messages")
async def get_messages() -> dict:
    return await retrieve_messages()


@router.post(
    "/",
    response_model=MessageSchema,
    status_code=201,
)
async def add_message_data(message: AddMessageSchema = Body(...)) -> dict:
    await FastAPICache.clear(namespace="fastapi_get_messages")
    message = jsonable_encoder(message)
    return await add_message(message)
