#!/usr/bin/python3
"""
This module contains a file storage system for Base Model and
it subclasses
"""
import cmd
import models.user
import models.state
import models.city
import models.place
import models.amenity
import models.review
from os import path
import json

BaseModel = models.user.BaseModel
User = models.user.User
State = models.state.State
City = models.city.City
Place = models.place.Place
Amenity = models.amenity.Amenity
Review = models.review.Review


class FileStorage:
    """
    A file storage system to persist objects created
    during execution of airbnb console
    """
    __objects = {}
    __obj = {}
    __file_path = "file.json"
    classes = ({"Amenity": Amenity, "BaseModel": BaseModel, "User": User,
                "City": City, "Place": Place,
                "Review": Review, "State": State})

    def all(self):
        """
        Returns a dictionary of all objects that has been created
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.to_dict()["__class__"] + "." + str(obj.id)
        my_dict = obj.to_dict()
        FileStorage.__objects.update({key: obj})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        filename = FileStorage.__file_path
        # write __objectsect to json file
        new_obj = {x: y.to_dict() for x, y in FileStorage.__objects.items()}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(new_obj, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """

        filename = FileStorage.__file_path
        # check if file_path exists
        if not path.exists(filename):
            return
        # opens the file and parses json string into a dictionary
        with open(filename, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            objects_dict = {}
            for x, y in obj_dict.items():
                NewModel = FileStorage.classes[y.get("__class__")]
                new_instance = NewModel(**y)
                objects_dict.update({x: new_instance})
            FileStorage.__objects = objects_dict
