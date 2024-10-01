#!/usr/bin/python3
""" module for FileStorage """

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State


class FileStorage:
    """ file storage class """

    __file_path = "file.json"
    __objects = {}
    __class_dictionary = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity,
        "City": City,
        "State": State
    }

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    if cls_name in self.__class_dictionary:
                        self.new(self.__class_dictionary[cls_name](**o))
        except FileNotFoundError:
            return
