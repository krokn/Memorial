from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.connection import Base


class UserModel(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    fatherName: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    idEducationInstitution: Mapped[int] = mapped_column(ForeignKey("educationInstitution.id"))

    EducationInstitution: Mapped["EducationInstitutionModel"] = relationship('EducationInstitutionModel', uselist=False)


class EducationInstitutionModel(Base):
    __tablename__ = 'educationInstitution'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


class PostModel(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    linkToPhoto: Mapped[str] = mapped_column()
    isApproved: Mapped[bool] = mapped_column(default=False)
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    idUser: Mapped[int] = mapped_column(ForeignKey('user.id'))


class PostUserModel(Base):
    __tablename__ = 'postUser'

    id: Mapped[int] = mapped_column(primary_key=True)
    idUser: Mapped[int] = mapped_column(ForeignKey('user.id'))
    idPost: Mapped[int] = mapped_column(ForeignKey('post.id'))

