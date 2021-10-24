from fastapi import FastAPI

from main.libs.chat_room import ChatRoom

chat_room = ChatRoom()

app = FastAPI()


# Avoiding circular imports
def register_controllers():
    import main.controllers


register_controllers()
