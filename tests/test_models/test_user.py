#!/usr/bin/python3
"""unit test for user class"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Test case for User"""
    self.user = User()

def test_user_values(self):
    """ Method: Start test for "user" """
    self.user = User()
    self.assertEqual(self.user.email, "")
    self.assertEqual(self.user.password, "")
    self.assertEqual(self.user.first_name, "")
    self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()
