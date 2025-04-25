import unittest

from array_intersection import array_intersection

class TestBasicFunctionality(unittest.TestCase):
    def test_array_intersection(self):
        a = array_intersection([1,2,2,1], [2,2])
        self.assertEqual( [2,2], a)
        b = array_intersection([4,9,5], [9,4,9,8,4])
        self.assertIn(b, [[9,4], [4,9]])
        c = array_intersection( [1,1], [1])
        self.assertEqual( [1], c)
        d = array_intersection([1, 1], [1, 2])
        self.assertEqual([1], d)
