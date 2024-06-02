import os

from dotenv import load_dotenv

from src.server.config.logger import get_logger

logger = get_logger(__name__)
load_dotenv()

EXAMPLE_SCHEMA = "example"

API_BASE_PATH = os.environ["API_BASE_PATH"]
DATABASE_URL = os.environ["DATABASE_URL"]