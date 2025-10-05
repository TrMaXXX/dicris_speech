from pydantic import BaseModel, Field


class InputModel(BaseModel):
    meteo_fve_input_file: str = Field(
        title="Meteo and FVE data",
        description="The path to the joined Meteo and FVE data",
        # json_schema_extra={"from_upstream": "always"}
    )


class OutputModel(BaseModel):
    """
    IsDay Piece Output Model
    """
    number: int = Field(
        default=0,
        description="Random number"
    )
