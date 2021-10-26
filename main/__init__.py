import logging

from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html

from main.config import Config
from main.services.chat import ChatRoom

logger = logging.getLogger("uvicorn.error")
config = Config()

chat_room = ChatRoom()
app = FastAPI(docs_url=None, redoc_url=None)


# Avoiding circular imports
def register_controllers():
    import main.controllers

    @app.get("/redoc")
    async def get_documentation():
        return get_redoc_html(openapi_url="openapi.json", title="docs")


register_controllers()
