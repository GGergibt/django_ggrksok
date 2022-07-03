from sqlmodel import Field, Relationship, SQLModel

# from sqlalchemy.dialects.postgresql import UUID
from datetime import date, datetime
from sqlalchemy import UniqueConstraint

import uuid


from pydantic import EmailStr


class User_table(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("email"),)
    id: int | None = Field(primary_key=True)
    name: str | None = Field(index=True)
    email: EmailStr = Field()
    password: str = Field()


class Tokens(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    token: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, nullable=False)
    expires: date = Field()
    user_id: int = Field(foreign_key="user_table.id", index=True)

    class Config:
        allow_population_by_field_name = True

    # # @validator("token")
    # def hexlify_token(cls, value):
    #     """Конвертирует UUID в hex строку"""
    #     return value.hex
