#!/usr/bin/python3
""" unit test for base model class"""

import os
import pep8
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage_instantiation(unittest.TestCase):
    """ define setup and teardown """

    def setUp(self):
        """ sets up the class """
        self.my_model = FileStorage()

    def tearDown(self):
        """ tears down the class """
        del self.my_model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
