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

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Setup the test"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        self.user = User("email@example.com", "password", "John", "Doe")
        self.user.id = "12345"
        self.storage.new(self.user)
        self.storage.save()
        self.state = State("CA", "California")
        self.state.id = "123456"
        self.storage.new(self.state)
        self.storage.save()