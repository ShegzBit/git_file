#!/usr/bin/python3
"""
This module contains City class for Airbnb console
project
"""
from models.state import BaseModel


class City(BaseModel):
    """
    City class for Airbnb project
    """
    state_id = ""
    name = ""
