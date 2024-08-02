from pydantic import BaseModel


class MessageSchema(BaseModel):
    # id: str
    # telegram_id: int
    username: str
    message: str


class AddMessageSchema(BaseModel):
    # telegram_id: int
    username: str
    message: str


class ListMessageSchema(BaseModel):
    messages: list[MessageSchema]
