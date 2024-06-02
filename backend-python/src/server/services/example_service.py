import uuid

from src.server.config.logger import get_logger
from src.server.repositories.example_repository import example_repository

logger = get_logger(__name__)


def get_latest_example():
    """Get the latest example.

    Returns:
        str: The latest example.
    """
    try:
        examples = example_repository.fetch_uuids()[-1].greeting
    except IndexError:
        return str(uuid.uuid4())
    except Exception as e:
        logger.error(f"Failed to fetch example uuids: {e}")
        return "Failed to fetch example uuids"
    return examples[-1]