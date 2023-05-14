#!/usr/bin/python3
"""Create a Review class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherits all 
	the properties of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
