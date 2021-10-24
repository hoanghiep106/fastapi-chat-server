from fastapi import FastAPI

from main.config import Config
from main.libs.chat_room import ChatRoom

config = Config()
chat_room = ChatRoom()

app = FastAPI()


# Avoiding circular imports
def register_controllers():
    import main.controllers


register_controllers()
