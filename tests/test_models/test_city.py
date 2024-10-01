#!/usr/bin/python3
""" City unittest """
import unittest
from models import City

class TestCity(unittest.TestCase):
    """ class defined to test City """
    def setUp(self):
        """ Set up for the tests """
        self.city = City()