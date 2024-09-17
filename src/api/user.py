from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from loguru import logger
from starlette.responses import JSONResponse

from src.core.user import UserCore
from src.repository.user import UserRepository
from src.schemas.user import UserSchemaForAuth, UserSchemaEmail
from src.services.cash import create_code_for_email_and_save_code, redis_client
from src.services.encrypt import Encrypt
from src.services.Celery import send_email

router = APIRouter(
    prefix="/api/user",
    tags=["Auth"],
)


@router.post('')
async def authUser(user: UserSchemaForAuth):
    if await UserRepository().get(user.email) is not None:
        raise HTTPException(status_code=403, detail=f"user register, can login")
    send_email.delay(user.email, create_code_for_email_and_save_code(user.email))
    return JSONResponse(status_code=HTTPStatus.OK, content='code send success')


@router.post('login')
async def loginUser(user: UserSchemaEmail):
    if await UserRepository().get(user.email) is None:
        raise HTTPException(status_code=405, detail=f"user dont register, can register")
    send_email.delay(user.email, create_code_for_email_and_save_code(user.email))
    return JSONResponse(status_code=HTTPStatus.OK, content='code send success')


@router.post('/code')
async def verifyCode(code: int, user: UserSchemaForAuth):
    saved_code = redis_client.get(user.email)
    logger.info(f'saved_code = {saved_code}, code_user = {code}')
    if int(saved_code) != code:
        raise HTTPException(status_code=406, detail="incorrect code")
    await UserCore().addUser(user)
    token = Encrypt().create_token(user.email)
    return JSONResponse(status_code=HTTPStatus.OK, content=token)
