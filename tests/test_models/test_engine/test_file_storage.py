#!/usr/bin/python3
""" unit test for base model class"""

import os
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
        """Set up the test"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        self.user = User("email@example.com", "password", "first", "last")
        self.user_id = self.user.id
        self.storage.new(self.user)
        self.storage.save()
        self.state = State("OK", "Oklahoma")
        self.state_id = self.state.id
        self.storage.new(self.state)
        self.storage.save()
