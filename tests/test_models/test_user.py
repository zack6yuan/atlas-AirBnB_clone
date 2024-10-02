#!/usr/bin/python3
"""unit test for user class"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Test case for User"""
    self.user = User()

    def test_user_setup(self):
        """ Method: Start test for "user" """
        self.user = User()
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_values(self):
        """ Check that attributes were assigned correctly """
        self.user.email = "john.appleseed@mail.com"
        self.user.password = "Apple123"
        self.user.first_name = "John"
        self.user.last_name = "Appleseed"

        self.assertEqual(self.user.email, "johnappleseed@mail.com")
        self.assertEqual(self.user.password, "Apple123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqial(self.user.last_name, "Appleseed")

if __name__ == "__main__":
    unittest.main()
