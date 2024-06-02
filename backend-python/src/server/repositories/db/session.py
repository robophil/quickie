from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.server.config.config import DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
ScopedSession = scoped_session(SessionLocal)


def get_db() -> Generator:
    """Provides a generator yielding a database session from a scoped session
    factory.

    This function is designed to be used with a context manager to ensure that database
    sessions are properly closed after use, preventing leaks. It sets an attribute
    `current_user_id` to None for each session, which can be used to track the user
    associated with a session in the application.

    Yields:
        Generator[scoped_session, None, None]: A generator yielding a scoped session object.
    """
    db = ScopedSession()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()


@contextmanager
def use_session(session_generator):
    """Context manager for managing database sessions.

    This context manager simplifies handling database sessions by encapsulating the
    creation and teardown process. It utilizes a session generator to obtain a database
    session, yields it for use in a with-block, and ensures the session is closed after
    use. This helps in managing resources efficiently and avoiding database session leaks.

    Args:
        session_generator (callable): A callable that when called returns a generator
                                      yielding database sessions.

    Yields:
        scoped_session: The database session obtained from the session generator.
    """
    db = None
    try:
        db = next(session_generator())
        yield db
    finally:
        if db is not None:
            db.close()