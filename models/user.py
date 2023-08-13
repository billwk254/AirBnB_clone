#!/usr/bin/python3

from models.base_model import BaseModel
"""User class for users"""


class User(BaseModel):
    """Class User that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
