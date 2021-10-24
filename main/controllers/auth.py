from main import app
from main.database import serialize_doc
from main.schemas.user import UserModel, AuthModel
from main.services import user as user_service


@app.post("/auth", response_model=UserModel)
async def auth(user: AuthModel):
    user_doc = await user_service.get_user_by_name(user.name)
    if not user_doc:
        user_doc = await user_service.create_user(user)
    return serialize_doc(user_doc)
