import inflection
from sqlalchemy.ext.declarative import declared_attr
from sqlmodel import SQLModel

from ..constants.db import table_prefix


class Base(SQLModel):
    @declared_attr
    def __tablename__(cls):
        return f"{table_prefix}{inflection.pluralize(inflection.underscore(cls.__name__))}"

