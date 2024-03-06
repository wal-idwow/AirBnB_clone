#!/usr/bin/python3
"""class review inherits from basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """represent review"""

    place_id = ""
    user_id = ""
    text = ""
