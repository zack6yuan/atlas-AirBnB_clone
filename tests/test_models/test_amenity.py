#!/usr/bin/python3
""" Amenity unittest """
import unittest

class TestAmenity(unittest.TestCase):
    """ Test case for Amenity """

    def setUp(self):
        """ Set up for the tests """
        self.amentiy = Amentiy()

    def test_amentiy_values(self):
        """ Method: Start test for "amenity" """
        self.amenity = Amenity()
        self.assertEqual(self.amenity.name, "")

        if __name__ == "__main__":
            unittest.main()
