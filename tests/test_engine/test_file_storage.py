#!/usr/bin/python3
""" unit test for base model class"""

import unittest
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class """

    def test_normal_cases_base_model(self):
        """ Test normal cases """
        my_model = FileStorage()
        my_dict = my_model.all()
        self.assertIs(type(my_dict), dict)
