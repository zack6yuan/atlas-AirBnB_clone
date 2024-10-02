#!/usr/bin/python3
""" unittest for state """
import unittest

class TestState(unittest.TestCase):
    """ Class defined for "state" testcase """
    def setUp(self):
        """ Method: represent "state" testcase """
        self.state = State()
        self.assertEqual(self.state.name, "")

    def test_state_values(self):
        """ Method: Start test for "state" """
        self.state = State()
        self.assertEqual(self.place.name, "")

if __name__ == "__main__":
    unittest.main()
