#!/usr/bin/python3
"""
A module for Base model for all classes in AirBnB console
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all other classes in AirBnB project to inherit from
    it contain all neccessary method for smooth operation of each class
    """

    def __init__(self, *args, **kwargs):
        """
        Class constructor for base module
        Init the public instance attribute `id`
        loads an instance from kwargs dictionary
        args is never used
        """
        def str_to_date(iso_str: str):
            """
            converts isoformat str to date
            """
            date_str, time_str = iso_str.split("T")
            date_list = date_str.split("-")
            time_str, micro_seconds = time_str.split(".")
            time_list = time_str.split(":")
            time_list.append(micro_seconds)
            date_list.extend(time_list)
            datetime_list = [int(x) for x in date_list]
            return datetime(*datetime_list)

        # loop through kwargs and set
        # attribute the attribute is not the id or __class__ or created_at
        for x, y in kwargs.items():
            if x not in ("__class__", "created_at", "updated_at"):
                setattr(self, x, y)
            elif x in ("created_at", "updated_at"):
                y = str_to_date(y)
                setattr(self, x, y)
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        String representation of BaseModel class
        """
        class_name = self.__class__.__name__
        id = self.id
        my_dict = self.__dict__

        return f'[{class_name}] ({id}) {my_dict}'

    def __repr__(self):
        """
        String representation of BaseModel class
        """
        class_name = self.__class__.__name__
        id = self.id
        my_dict = self.__dict__

        return f'[{class_name}] ({id}) {my_dict}'

    def save(self):
        """
        Update the public instance `updated_at` with
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a comprehensive dictionary of the class
        """

        new_dict = {}
        for x, y in self.__dict__.items():
            new_dict.update({x: y})
        class_name = self.__class__.__name__
        created = self.created_at.isoformat()
        updated = self.updated_at.isoformat()
        new_dict.update({"__class__": class_name})
        new_dict.update({"created_at": created})
        new_dict.update({"updated_at": updated})

        return new_dict
