from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import random


class RandomNumPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        number=int(random.random()*100)
        # Set display result
        # Return output
        return OutputModel(
            number=number
        )
