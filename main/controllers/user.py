from main import app, config
from main.database import serialize_doc
from main.schemas.user import UserPaginationModel
from main.services import user as user_service


@app.get("/users", response_model=UserPaginationModel)
async def get_users(
        limit: int = config.DEFAULT_PAGE_LIMIT,
        skip: int = 0,
):
    docs = await user_service.get_users(limit=limit, skip=skip)
    total = await user_service.count_users()
    return {
        "items": [serialize_doc(doc) for doc in docs],
        "total": total,
        "skip": skip,
        "limit": limit,
    }
