from uuid import uuid4

from sqlalchemy import Column, String

from src.server.config.config import EXAMPLE_SCHEMA
from src.server.repositories.db.base_repository import Base


class ExampleModel(Base):
    """Represents the 'Example' table within the specified schema.

    Attributes:
        __tablename__ (str): Name of the table this model represents.
        uuid (Column): Unique identifier
        greeting (Column): A greeting message
    """

    __tablename__ = f"{EXAMPLE_SCHEMA}.EXAMPLE"

    uuid = Column(String(36), primary_key=True, default=str(uuid4()))
    greeting = Column(String(255), nullable=False)