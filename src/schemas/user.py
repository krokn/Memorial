from pydantic import BaseModel, EmailStr


class UserSchemaForAuth(BaseModel):
    name: str
    surname: str
    fatherName: str
    nameEducationInstitution: str
    email: EmailStr


class UserSchemaForLoginSendCode(BaseModel):
    email: EmailStr


class UserSchema(BaseModel):
    name: str
    surname: str
    fatherName: str
    idEducationInstitution: int
    email: EmailStr


class UserSchemaEmail(BaseModel):
    email: EmailStr
