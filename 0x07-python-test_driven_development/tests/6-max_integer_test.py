#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-5, 4, 10]), 10)
        self.assertEqual(max_integer([-15, -12]), -12)
        self.assertEqual(max_integer([4.1, 4, 2, 3]), 4.1)
        self.assertEqual(max_integer([5729810298347362832973, 2345, 1234]), 5729810298347362832973)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([True, False, 200]), 200)

        self.assertRaises(TypeError, max_integer, [1, 2, "a"])
        self.assertRaises(TypeError, max_integer, (1,2,3,4))

if __name__ == "__main__":
    unittest.main()
