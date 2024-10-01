#!/usr/bin/python3
"""unit test for base model class"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User
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

    def test_save(self):
        """Test save method"""
        self.updated_at = datetime.now()
        models.FileStorage.save(models.storage)

    def test_to_dict(self):
        """Test to_dict method"""
        my_model = BaseModel()
        dict_model = my_model.to_dict()
        self.assertIn('__class__', dict_model)
        self.assertIn('id', dict_model)
        self.assertIn('created_at', dict_model)
        self.assertIn('updated_at', dict_model)
