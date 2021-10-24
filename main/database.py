from typing import Any, Dict

import motor.motor_asyncio

from main import config
from main.enums import Collection

client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGO_URI)

database = client.chat
user_collection = database.get_collection(Collection.USER)
message_collection = database.get_collection(Collection.MESSAGE)


def serialize_doc(doc: Dict[str, Any]):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc
