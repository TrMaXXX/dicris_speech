from pydantic import BaseModel, Field


class InputModel(BaseModel):
    max_num: int = Field(
        default=100,
        title="Maximum",
        description="Maximum for random generator",
        # json_schema_extra={"from_upstream": "always"}
    )


class OutputModel(BaseModel):
    """
    IsDay Piece Output Model
    """
    number: float = Field(
        default=0.0,
        description="Random number"
    )
