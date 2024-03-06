#!/usr/bin/python3
"""class city inherits from basemodel"""

from models.base_model import BaseModel


class City(BaseModel):
    """represent a city"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)