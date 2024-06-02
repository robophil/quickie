from uuid import uuid4

from sqlalchemy.engine import Engine

from src.server.config.constants import example_greeting_message
from src.server.config.logger import get_logger
from src.server.repositories.db.base_repository import Base
from src.server.repositories.db.session import engine
from src.server.repositories.example_repository import example_repository
from src.server.repositories.models.example_model import ExampleModel

logger = get_logger(__name__)


def create_schemas(
    db_engine: Engine = engine,
) -> None:
    """Creates all tables in the database.

    This function uses the SQLAlchemy ORM to create all tables defined in the models.
    It leverages the provided SQLAlchemy engine to execute the table creation queries directly.

    Args:
        db_engine (Engine): The SQLAlchemy Engine instance for database connections. This engine
                            should be configured with the necessary connection settings.
    """
    Base.metadata.create_all(bind=db_engine)
    logger.info("All tables created or already exist.")


def initialize_database() -> None:
    """Initializes the database by creating all tables defined in SQLAlchemy
    models across all schemas.

    This function ensures that the database is properly set up with the required schemas and tables
    according to the SQLAlchemy models defined in the application. It calls `create_schemas` to
    ensure necessary schemas are present before using SQLAlchemy's `create_all` method to create
    any tables defined in models.
    """
    logger.debug("Creating database schema from ORM base model")
    create_schemas()
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialization complete.")

    # Insert example data TODO: remove this
    example_repository.add_example(ExampleModel(uuid=str(uuid4()), greeting=example_greeting_message))
    logger.info("Example data inserted.")