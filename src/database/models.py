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
    isAdmin: Mapped[bool] = mapped_column(default=False)
    idEducationInstitution: Mapped[int] = mapped_column(ForeignKey("educationInstitution.id"))

    post: Mapped["PostModel"] = relationship("PostModel", back_populates="user", uselist=True, )

    EducationInstitution: Mapped["EducationInstitutionModel"] = relationship('EducationInstitutionModel', uselist=False, lazy="joined")


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
    isApproved: Mapped[str] = mapped_column(default='False')
    x: Mapped[float] = mapped_column()
    y: Mapped[float] = mapped_column()
    idUser: Mapped[int] = mapped_column(ForeignKey('user.id'))
    address: Mapped[str] = mapped_column()

    user: Mapped["UserModel"] = relationship("UserModel", back_populates="post", uselist=True, lazy="joined")



