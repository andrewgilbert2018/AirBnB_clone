#!/usr/bin/python3
"""Create a user class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits all the properties
    of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
