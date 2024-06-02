from fastapi import APIRouter

from src.server.config.logger import get_logger
from src.server.services.example_service import get_latest_example

logger = get_logger(__name__)

router = APIRouter(
    prefix="/main",
    tags=["main"],
)


@router.get(path="/example", summary="Get example uuid", response_model=str)
async def get_greeting_message() -> str:
    """Get a greeting message.

    Returns:
        str: A greeting message.
    """

    return get_latest_example()
