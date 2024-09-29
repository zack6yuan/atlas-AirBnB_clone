#!/usr/bin/python3

"""module for init file"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State

storage = FileStorage()
storage.reload()

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity,
    "City": City,
    "State": State
}
