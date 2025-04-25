import unittest

from solutions.rotate_array import rotate_array

class TestBasicFunctionality(unittest.TestCase):
    def test_rotate_array(self):
        a = [1,2,3,4,5,6,7]
        rotate_array(a, 3)
        self.assertEqual(a, [5,6,7,1,2,3,4])