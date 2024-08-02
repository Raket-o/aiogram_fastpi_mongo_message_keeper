"""Database Transaction Module."""

from app.database.connect import message_keeper_collection


def message_helper(message) -> dict:
    """The function returns the parsed data."""
    return {
        "id": str(message["_id"]),
        "username": message["username"],
        "message": message["message"],
    }


async def retrieve_messages() -> dict[str, list[dict]]:
    """The function of requesting messages from the collection."""
    messages = []
    async for message in message_keeper_collection.find():
        messages.append(message_helper(message))
    return {"messages": messages}


async def add_message(message_data: dict) -> dict:
    """The function of creating a message to a collection."""
    message = await message_keeper_collection.insert_one(message_data)
    new_message = await message_keeper_collection.find_one(
        {"_id": message.inserted_id}
    )
    return message_helper(new_message)
