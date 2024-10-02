#!/usr/bin/python3
""" unittest for place """
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """ Class defined for "place" testcase """
    def test_place_setup(self):
        """ Method: represent place "testcase" """
        self.place = Place()
        self.assertEqual(type(self.place), Place)

    def test_place_values(self):
        self.place = Place()
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        
if __name__ == "__main__":
    unittest.main()
