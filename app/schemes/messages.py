"""The Schematics module."""

from pydantic import BaseModel


class MessageSchema(BaseModel):
    username: str
    message: str


class AddMessageSchema(BaseModel):
    username: str
    message: str


class ListMessageSchema(BaseModel):
    messages: list[MessageSchema]
