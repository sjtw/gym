import unittest

from max_profit import max_profit


class TestBasicFunctionality(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([2,10,1,1,3]), 10)
        self.assertEqual(max_profit([5,4,1]), 0)
        self.assertEqual(max_profit([1,2,3,3]), 2)
