#!/usr/bin/python3
""" unittest for review """
import unittest
from models.review import Review
class TestReview(unittest.TestCase):
    """ Test case for Review """
    def setUp(self):
        """ Set up for the tests """
        self.review = Review()

    def test_review_values(self):
        """ Method: Start test for "review" """
        self.review = Review()
