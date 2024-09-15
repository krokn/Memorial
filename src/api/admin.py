from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse
from websockets.legacy.server import HTTPResponse

from src.core.admin import AdminCore
from src.repository.post import PostRepository

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"],
)

@router.get('/post')
async def getAllPostForAdmin():
    posts = await AdminCore().getAllPost()
    return JSONResponse(status_code=HTTPStatus.OK, content=posts)

@router.patch('{id}')
async def changeApproved(idPost: int):
    await AdminCore().changeApproved(idPost)
    return JSONResponse(status_code=HTTPStatus.OK, content='change approved success')