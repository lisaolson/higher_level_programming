#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
"""Checks for correct output and errors
"""

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-5, 4, 10]), 10)
        self.assertEqual(max_integer([-15, -12]), -12)
        self.assertEqual(max_integer([4.1, 4, 2, 3]), 4.1)
        self.assertEqual(max_integer([57298102983, 2345, 1234]), 57298102983)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([True, False, 200]), 200)
        self.assertEqual(max_integer((1,2,3,4,5)), 5)
        self.assertEqual(max_integer([[1, 2, 3, 4], [1, 2, 3, 50]]),\
        [1, 2, 3, 50])
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([3]), 3)

        self.assertRaises(TypeError, max_integer, [1, 2, "a"])
        self.assertTrue(len(max_integer.__doc__) != 0)

if __name__ == "__main__":
    unittest.main()
