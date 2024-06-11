from datetime import datetime

from sqlalchemy import Column, TIMESTAMP, func
from sqlmodel import Field
from .mixins import Base


class User(Base, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    email: str
    email_verified: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), nullable=False))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(
        sa_column=Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False))


