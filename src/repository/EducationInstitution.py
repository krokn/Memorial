from typing import List

from sqlalchemy import select

from src.database.connection import get_async_session
from src.database.models import EducationInstitutionModel


class EducationInstitutionRepository:

    @staticmethod
    async def get(name: str) -> EducationInstitutionModel:
        async with get_async_session() as session:
            query = select(EducationInstitutionModel).where(EducationInstitutionModel.name == name)
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    async def get_all() -> List[EducationInstitutionModel]:
        async with get_async_session() as session:
            query = select(EducationInstitutionModel).where(EducationInstitutionModel.name == name)
            result = await session.execute(query)
            return result.scalars().all()
