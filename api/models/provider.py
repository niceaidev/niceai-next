from datetime import datetime
from typing import Optional

from sqlalchemy import Column, func, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSON
from sqlmodel import Field
from .mixins import Base


class Provider(Base, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    description: str
    provider_name: str
    provider_type: str
    encrypted_config: Optional[dict] = Field(sa_column=Column(JSON))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False))

