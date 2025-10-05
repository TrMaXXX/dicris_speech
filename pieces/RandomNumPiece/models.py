from pydantic import BaseModel, Field


class InputModel(BaseModel):


class OutputModel(BaseModel):
    """
    IsDay Piece Output Model
    """
    number: int = Field(
        default=0,
        description="Random number"
    )
