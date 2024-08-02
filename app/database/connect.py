import motor.motor_asyncio

from config_data.config import MONGO_URI, MONGO_DB_NAME


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

database = client.message_keeper

message_keeper_collection = database.get_collection(MONGO_DB_NAME)
