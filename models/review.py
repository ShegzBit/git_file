#!/usr/bin/python3
"""
This module contains Review class for Airbnb
"""
from models.place import BaseModel


class Review(BaseModel):
    """
    Review class for amenity object in Airbnb
    """
    name = ""
    place_id = ""
    user_id = ""
    text = ""
