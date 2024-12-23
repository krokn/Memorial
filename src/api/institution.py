from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.repository.EducationInstitution import EducationInstitutionRepository
from src.response.post import get_all_institution_response

router = APIRouter(
    prefix="/api/institution",
    tags=["Institution"],
)


@router.get('')
async def get_all_institution():
    models = await EducationInstitutionRepository().get_all()
    dict = await get_all_institution_response(models)
    return JSONResponse(status_code=HTTPStatus.OK, content=dict)


