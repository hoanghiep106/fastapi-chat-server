import logging

from starlette.responses import JSONResponse

from main import app
from . import chat, auth, user, message


@app.exception_handler(Exception)
async def exception_handler(_, e: Exception):
    logging.exception(e)
    return JSONResponse(
        status_code=500,
        content={"detail": "Something went wrong"},
    )
