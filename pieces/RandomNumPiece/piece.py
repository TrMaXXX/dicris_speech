from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import random
import base64


class RandomNumPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        number=int(random.random()*input_data.max_num)
        # Set display result
        # Return output
        raw_content = f"Random number is: {number}\n"
        base64_content = base64.b64encode(raw_content.encode("utf-8")).decode("utf-8")
        self.display_result = {
            "file_type": "txt",
            "base64_content": base64_content
        }

        self.logger.info(f"Random number is: {number}")
        return OutputModel(
            number=number
        )
