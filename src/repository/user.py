from typing import List

from sqlalchemy import select

from src.database.connection import get_async_session
from src.database.models import UserModel, PostModel


class UserRepository:

    @staticmethod
    async def add(user: UserModel):
        async with get_async_session() as session:
            async with session.begin():
                session.add(user)
                await session.flush()
                await session.commit()

    @staticmethod
    async def get(email: str) -> UserModel:
        async with get_async_session() as session:
            query = select(UserModel).where(UserModel.email == email)
            result = await session.execute(query)
            return result.scalars().one_or_none()


