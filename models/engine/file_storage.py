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

    def all(self):
        """ returns the dictionary """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                name = key.split(".")[0]
                self.__objects[key] = eval(name)(**value)