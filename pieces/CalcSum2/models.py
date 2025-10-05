from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    IsDay Piece Input Model
    """

    meteo_fve_input_file_sum: str = Field(
        title="Meteo and FVE data SUM",
        description="The path to the joined Meteo and FVE data SUM",
        # json_schema_extra={"from_upstream": "always"}
    )


class OutputModel(BaseModel):
    """
    IsDay Piece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log SUM"
    )

    file_path: str = Field(
        description="The path to the Meteo and FVE data with added is day column SUM"
    )
