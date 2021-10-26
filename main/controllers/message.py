from main import app, config
from main.database import serialize_doc
from main.schemas.message import MessagePaginationModel
from main.services import message as message_service

DEFAULT_SORT = "-created_at"


@app.get("/messages", response_model=MessagePaginationModel)
async def get_messages(
        limit: int = config.DEFAULT_PAGE_LIMIT,
        skip: int = 0,
        sort: str = DEFAULT_SORT
):
    docs = await message_service.get_messages(skip, limit, sort)
    total = await message_service.count_messages()
    return {
        "items": [serialize_doc(doc) for doc in docs],
        "total": total,
        "skip": skip,
        "limit": limit,
    }
