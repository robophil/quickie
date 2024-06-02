from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
from starlette.routing import Mount

from src.server.config.config import API_BASE_PATH
from src.server.config.logger import configure_logging, get_logger
from src.server.startup.startup_tasks import initialize_database

from .routers import main_routers

configure_logging()
logger = get_logger(__name__)


_router_prefix = API_BASE_PATH
logger.info(f"starting application on base path {_router_prefix}")


def custom_generate_unique_id(route: APIRouter):
    """Generates a unique identifier for a given FastAPI route.

    This function constructs the identifier by combining the first tag of the route with the route's name,
    separated by a dash. It's used to ensure unique identification of API routes in the OpenAPI specification.

    Args:
        route (APIRouter): The FastAPI route for which a unique identifier is being generated.

    Returns:
        str: A string representing the unique identifier for the given route.
    """
    return f"{route.tags[0]}-{route.name}"


tags_metadata = [
    {
        "name": "main_routers",
        "description": "API layer for all main routers",
    },
]


def create_api():
    """Creates and configures an instance of the FastAPI application.

    This function sets up the FastAPI application with custom configurations, including title, description,
    version, and OpenAPI tags metadata. It also configures CORS middleware, registers exception handlers, and
    includes routers for different segments of the API.

    Returns:
        FastAPI: An instance of the FastAPI application configured with CORS, exception handlers, and included routers.
    """
    api = FastAPI(
        title="Example API",
        description="""""",
        version="0.0.1",
        openapi_tags=tags_metadata,
        generate_unique_id_function=custom_generate_unique_id,
        openapi_url=f"{_router_prefix}/api/openapi.json",
    )

    # Configure CORS
    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    router = APIRouter()
    router.include_router(
        main_routers.router,
    )
    api.include_router(router)
    return api


def create_app(mount_point):
    api = create_api()
    routes = [Mount(f"{_router_prefix}/api", app=api, name="api")]

    app = Starlette(debug=True, routes=routes)

    @app.on_event("startup")
    async def on_startup():
        logger.info("Starting application setup...")
        try:
            initialize_database()
            logger.info("Database and storage container initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize resources: {e}")
            raise

    return app


if __name__ == "__main__":
    app = create_api()
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
