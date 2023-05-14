#!/usr/bin/python3
"""Create a class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class city inherits all the properties
    of  BaseModel"""

    state_id = ""
    name = ""
