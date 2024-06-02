from pydantic import BaseModel


class ExampleResponse(BaseModel):
    """Represents the response model for an example.

    Attributes:
        uuid (str): Unique identifier
    """

    uuid: str
