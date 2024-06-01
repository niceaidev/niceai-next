from datetime import datetime

from sqlalchemy import Column, TIMESTAMP, func
from sqlalchemy.schema import CreateTable
from sqlmodel import SQLModel, Field

from models.mixins import Base


class App(Base, SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    name: str
    description: str
    provider: str
    data_source_type: str
    created_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False))



# 生成创建表语句
create_table_sql = str(CreateTable(App.__table__))

print(create_table_sql)