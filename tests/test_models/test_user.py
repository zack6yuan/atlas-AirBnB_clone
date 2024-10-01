#!/usr/bin/python3
"""unit test for user class"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Test case for User"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "
        self.user.password = "password"
        self.user.save()
        self.id = self.user.id
        self.user = None