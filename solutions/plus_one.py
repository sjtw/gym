import unittest
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    remainder = 1
    for i in range(len(digits)
                   -1,-1,-1):
        if digits[i] + remainder == 10:
            remainder = 1
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
        else:
            digits[i] = digits[i] + remainder
            return digits

    return digits