#!/usr/bin/python3
"""unit test for base model class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test case for BaseModel"""

    def test_normal_cases_base_model(self):
        """Test normal cases"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        self.assertIs(type(my_model.id), str)
        self.assertIs(type(my_model.created_at), datetime)
        self.assertIs(type(my_model.updated_at), datetime)
        self.assertIs(type(my_model.to_dict()), dict)
        self.assertIs(type(my_model.__str__()), str)