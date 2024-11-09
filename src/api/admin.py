from http import HTTPStatus

from fastapi import APIRouter, Header, HTTPException
from starlette.responses import JSONResponse
from websockets.legacy.server import HTTPResponse

from src.core.admin import AdminCore
from src.repository.post import PostRepository
from src.repository.user import UserRepository
from src.services.encrypt import Encrypt

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"],
)


@router.get('/post')
async def getAllPostForAdmin(token: str | None = Header(default=None)):
    emailUser = Encrypt().get_user_by_token(token)
    user_model = await UserRepository().get(emailUser)
    if not user_model.isAdmin:
        raise HTTPException(status_code=407, detail=f"user is not admin")
    posts = await AdminCore().getAllPost()
    return JSONResponse(status_code=HTTPStatus.OK, content=posts)


@router.patch('{id}')
async def changeApproved(id_post: int, status: str, token: str | None = Header(default=None)):
    emailUser = Encrypt().get_user_by_token(token)
    user_model = await UserRepository().get(emailUser)
    if not user_model.isAdmin:
        raise HTTPException(status_code=407, detail=f"user is not admin")
    await AdminCore().changeApproved(id_post, status)
    return JSONResponse(status_code=HTTPStatus.OK, content='change approved success')