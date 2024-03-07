#!/usr/bin/python3
"""class amenity inherits from basemodel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
