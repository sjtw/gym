import unittest

from contains_duplicate import contains_duplicates

class TestBasicFunctionality(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertTrue(contains_duplicates([1,2,3,3]))
        self.assertFalse(contains_duplicates([9,29,31,1]))
