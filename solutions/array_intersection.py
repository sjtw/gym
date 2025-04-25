import unittest
from typing import List

def array_intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    inter = []
    occurrences = {}
    nums_a, nums_b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

    for a in nums_a:
        occurrences[a] = occurrences.get(a, 0) + 1

    for b in nums_b:
        intersection = occurrences.get(b, 0)
        if intersection > 0:
            inter.append(b)
            occurrences[b] = occurrences.get(b, 0) - 1

    return inter

