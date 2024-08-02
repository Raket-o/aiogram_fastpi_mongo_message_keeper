from app.database.connect import message_keeper_collection


def message_helper(message) -> dict:
    return {
        "id": str(message["_id"]),
        # "telegram_id": message["telegram_id"],
        "username": message["username"],
        "message": message["message"],
    }


async def retrieve_messages():
    messages = []
    async for message in message_keeper_collection.find():
        messages.append(message_helper(message))
    return {"messages": messages}


async def add_message(message_data: dict) -> dict:
    message = await message_keeper_collection.insert_one(message_data)
    new_message = await message_keeper_collection.find_one({"_id": message.inserted_id})
    return message_helper(new_message)
