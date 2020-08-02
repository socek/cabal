from sqlalchemy import Binary
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String

from cabal.app.db import SqlTable


class UserTable(SqlTable):
    __tablename__ = "users"

    name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    is_admin = Column(Boolean, nullable=False, default=False)
    password = Column(Binary(100), nullable=True)
