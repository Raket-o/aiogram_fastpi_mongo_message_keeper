"""Database connection module."""

import motor.motor_asyncio

from config_data.config import MONGO_DB_NAME, MONGO_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.message_keeper
message_keeper_collection = database.get_collection(MONGO_DB_NAME)
