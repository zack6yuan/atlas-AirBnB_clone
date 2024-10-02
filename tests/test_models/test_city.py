#!/usr/bin/python3
""" City unittest """
import unittest

class TestCity(unittest.TestCase):
    """ Test case for City """
    def setUp(self):
        """ Set up for the tests """
        self.city = City()

    def test_city_values(self):
        """ Method: Start test for "city" """
        self.city = City()
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

if __name__ == "__main__":
    unittest.main()
