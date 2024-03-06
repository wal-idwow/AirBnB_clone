#!/usr/bin/python3
"""class user inherits from basemodel"""

from models.base_model import BaseModel


class User(BaseModel):
    """represent user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
