from pydantic import BaseModel


class MessageSchema(BaseModel):
    id: str
    telegram_id: int
    message: str


class AddMessageSchema(BaseModel):
    telegram_id: int
    message: str


class ListMessageSchema(BaseModel):
    messages: list[MessageSchema]
    # message: str


# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }