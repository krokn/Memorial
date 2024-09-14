from http import HTTPStatus

from fastapi import APIRouter, Header
from starlette.responses import JSONResponse

from src.core.post import PostCore
from src.repository.post import PostRepository
from src.response.post import allPostsJson
from src.schemas.post import postSchemaToAdd
from src.services.encrypt import Encrypt

router = APIRouter(
    prefix="/api/post",
    tags=["Auth"],
)


@router.post('/user')
async def addPost(post: postSchemaToAdd, token: str | None = Header(default=None)):
    emailUser = Encrypt().get_user_by_token(token)
    await PostCore().addPost(post, emailUser)
    return JSONResponse(status_code=HTTPStatus.OK, content='post add success')


@router.get('')
async def getAllApprovedPost():
    posts = await PostRepository().getAll()
    dictPosts = await allPostsJson(posts)
    return JSONResponse(status_code=HTTPStatus.OK, content=dictPosts)



