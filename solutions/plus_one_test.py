import unittest

from solutions.plus_one import plus_one


class TestBasicFunctionality(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual(plus_one([1,2,3]), [1,2,4])
        self.assertEqual(plus_one([4,3,2,1]), [4,3,2,2])
        self.assertEqual(plus_one([9]), [1,0])
        self.assertEqual(plus_one([9,9]), [1,0,0])

