from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.core.user import UserCore
from src.schemas.user import UserSchemaForAuth
from src.services.encrypt import Encrypt

router = APIRouter(
    prefix="/api/user",
    tags=["Auth"],
)


@router.post('')
async def authUser(user: UserSchemaForAuth):
    await UserCore().addUser(user)
    token = Encrypt().create_token(user.email)
    return JSONResponse(status_code=HTTPStatus.OK, content=token)

