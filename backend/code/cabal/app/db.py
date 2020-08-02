from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


class Base:
    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False
    )

    def _asdict(self):
        data = dict(self.__dict__)
        del data["_sa_instance_state"]
        return data


SqlTable = declarative_base(cls=Base)
