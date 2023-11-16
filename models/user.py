#!/usr/bin/python3
"""
This module contains Airbnb User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class template for User object in Airbnb
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
