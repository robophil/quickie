from typing import List

from src.server.config.logger import get_logger
from src.server.repositories.db.base_repository import BaseRepository
from src.server.repositories.db.session import use_session
from src.server.repositories.models.example_model import ExampleModel

logger = get_logger(__name__)


class ExampleRepository(BaseRepository[ExampleModel]):
    """A repository class for managing and accessing association rules within
    the database.

    Inherits from `BaseRepository` and is specialized for handling `ExampleModel`
    instances, providing an interface to fetch and manage association rule data stored in the
    database.
    """

    def __init__(self):
        """Initializes the `ExampleRepository` repository with the
        `ExampleModel`."""
        super().__init__(ExampleModel)

    def fetch_uuids(self) -> List[ExampleModel]:
        """Fetches all association rules stored in the database.

        Uses a database session to query all rows in the association rules table, logging
        the number of records fetched. Intended to be extended or modified to include more
        complex querying and filtering logic as needed.

        Returns:
            List[ExampleModel]: A list of all association rules as SQLAlchemy model instances.
        """
        with use_session(self.db_session_generator) as db:
            example = db.query(ExampleModel).all()
            logger.info(f"Fetched {len(example)} example uuids.")
            # Convert SQLAlchemy model instances to Pydantic model instances
            return example

    def add_example(self, example: ExampleModel) -> ExampleModel:
        """Adds a new example to the database.

        Args:
            example (ExampleModel): The example to add.

        Returns:
            ExampleModel: The added example.
        """
        with use_session(self.db_session_generator) as db:
            db.add(example)
            db.commit()
            db.refresh(example)
            return example

example_repository = ExampleRepository()
