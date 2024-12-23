from typing import List, Dict, Any

from sqlalchemy import select

from src.database.connection import get_async_session
from src.database.models import UserModel, PostModel, EducationInstitutionModel


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

    @staticmethod
    async def get_with_education(email: str) -> dict[str, Any] | None:
        async with get_async_session() as session:
            query = (
                select(UserModel, EducationInstitutionModel.name.label("institutionName"))
                .join(EducationInstitutionModel, UserModel.idEducationInstitution == EducationInstitutionModel.id)
                .where(UserModel.email == email)
            )
            result = await session.execute(query)
            user_data = result.first()
            if user_data:
                user, institution_name = user_data
                return {
                    "id": user.id,
                    "name": user.name,
                    "surname": user.surname,
                    "fatherName": user.fatherName,
                    "email": user.email,
                    "isAdmin": user.isAdmin,
                    "institutionName": institution_name,
                }
            return None



