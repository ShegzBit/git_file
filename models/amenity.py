#!/usr/bin/python3
"""
This module contains Amenity class for Airbnb
"""
from models.city import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for amenity object in Airbnb
    """
    name = ""
