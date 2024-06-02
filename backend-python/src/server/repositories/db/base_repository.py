from typing import Generic, Type, TypeVar

from sqlalchemy.ext.declarative import declarative_base

from src.server.repositories.db.session import get_db

Base = declarative_base()

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """A generic base repository that provides CRUD (Create, Read, Update,
    Delete) operations.

    This base repository leverages SQLAlchemy models to abstract common database operations,
    allowing for easy extension and customization for specific entity types.

    Attributes:
        db_session_generator (function): A function that when called returns a database session generator.
                                         This is used to create sessions for executing database operations.
        model (Type[ModelType]): The SQLAlchemy model class that represents the entity for CRUD operations.
    """

    def __init__(self, model: Type[ModelType]):
        """Initializes a new instance of the BaseRepository with the specified
        model.

        Args:
            model (Type[ModelType]): The SQLAlchemy model class that defines the structure
                                     and relationships of the entity being managed. This model
                                     is used for all CRUD operations.
        """
        self.db_session_generator = get_db
        self.model = model
