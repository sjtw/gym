import unittest
from typing import List


def single_number(nums: List[int]) -> int:
    x = 0
    for num in nums:
        x ^= num
    return x

class TestBasicFunctionality(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(single_number([2,2,1]), 1)
        self.assertEqual(single_number([4,2,2,9,4]), 9)
