from typing import List

from sqlalchemy import select

from src.database.connection import get_async_session
from src.database.models import PostModel


class PostRepository:

    @staticmethod
    async def post(postModel: PostModel):
        async with get_async_session() as session:
            session.add(postModel)
            await session.flush()
            await session.commit()

    @staticmethod
    async def getAllApproved() -> List[PostModel]:
        async with get_async_session() as session:
            query = select(PostModel).where(PostModel.isApproved == 'True')
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def getAllApprovedByUser(id_user: int) -> List[PostModel]:
        async with get_async_session() as session:
            query = select(PostModel).where(PostModel.idUser == id_user)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def getAllNotApproved() -> List[PostModel]:
        async with get_async_session() as session:
            query = select(PostModel).where(PostModel.isApproved == 'in_progress')
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def getOne(idPost: int) -> PostModel:
        async with get_async_session() as session:
            query = select(PostModel).where(PostModel.id == idPost)
            result = await session.execute(query)
            return result.scalars().first()
