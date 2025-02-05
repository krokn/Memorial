from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Header
from loguru import logger
from starlette.responses import JSONResponse

from src.core.user import UserCore
from src.repository.user import UserRepository
from src.schemas.user import UserSchemaForAuth, UserSchemaEmail, UserSchemaForLoginSendCode
from src.services.cash import create_code_for_email_and_save_code, redis_client
from src.services.encrypt import Encrypt
from src.services.Celery import send_email, send_email_html

router = APIRouter(
    prefix="/api/user",
    tags=["Auth"],
)

def create_email_letter(code: str) -> str:
    return f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6;">
            <p>Пожалуйста, используйте этот код для подтверждения адреса вашей электронной почты:</p>
            <h2 style="color: #2E86C1; text-align: center;">{code}</h2>
            <hr style="border: 1px solid #ddd;">
            <p>Всероссийский патриотический проект «Карта памяти»</p>
            <p>Почта технической поддержки: <a href="mailto:memorial.i@yandex.ru">memorial.i@yandex.ru</a></p>
        </body>
    </html>
    """


@router.post('')
async def authUser(user: UserSchemaForAuth):
    if await UserRepository().get(user.email) is not None:
        raise HTTPException(status_code=403, detail=f"user register, can login")

    code = create_code_for_email_and_save_code(user.email)
    letter = create_email_letter(code)
    send_email_html.delay(user.email, letter)
    return JSONResponse(status_code=HTTPStatus.OK, content='Code sent successfully')


@router.post('login')
async def loginUser(user: UserSchemaEmail):
    if await UserRepository().get(user.email) is None:
        raise HTTPException(status_code=405, detail=f"user dont register, can register")
    code = create_code_for_email_and_save_code(user.email)
    letter = create_email_letter(code)
    send_email_html.delay(user.email, letter)
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


@router.post('/code-login')
async def verifyCode(code: int, user: UserSchemaForLoginSendCode):
    saved_code = redis_client.get(user.email)
    logger.info(f'saved_code = {saved_code}, code_user = {code}')
    if int(saved_code) != code:
        raise HTTPException(status_code=406, detail="incorrect code")
    token = Encrypt().create_token(user.email)
    return JSONResponse(status_code=HTTPStatus.OK, content=token)


@router.get('/info')
async def get_info(token: str | None = Header(default=None)):
    emailUser = Encrypt().get_user_by_token(token)
    user_data = await UserRepository().get_with_education(emailUser)
    if user_data:
        return JSONResponse(status_code=HTTPStatus.OK, content=user_data)
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"error": "User not found"})

