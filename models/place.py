#!/usr/bin/python3
"""
This module contains Place class for Airbnb
"""
from models.amenity import BaseModel


class Place(BaseModel):
    """
    Place class for Place object in Airbnb
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
