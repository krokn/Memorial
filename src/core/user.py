from src.database.models import UserModel, EducationInstitutionModel
from src.repository.EducationInstitution import EducationInstitutionRepository
from src.repository.user import UserRepository
from src.schemas.user import UserSchema, UserSchemaForAuth


class UserCore:

    @staticmethod
    async def addUser(userSchema: UserSchemaForAuth):
        educationInstitution = await EducationInstitutionRepository.get(userSchema.nameEducationInstitution)
        userModel = await UserCore().createUserModel(userSchema, educationInstitution)
        await UserRepository().add(userModel)

    @staticmethod
    async def createUserModel(user: UserSchemaForAuth, educationInstitution: EducationInstitutionModel) -> UserModel:
        userModel = UserModel(
            name=user.name,
            surname=user.surname,
            fatherName=user.fatherName,
            email=user.email,
            idEducationInstitution=educationInstitution.id
        )
        return userModel
