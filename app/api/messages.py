"""Users routs processing module."""

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

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
async def get_messages() -> dict:
    return await retrieve_messages()


@router.post(
    "/",
    response_model=MessageSchema,
    status_code=201,
)
async def add_message_data(message: AddMessageSchema = Body(...)) -> dict:
    message = jsonable_encoder(message)
    return await add_message(message)
