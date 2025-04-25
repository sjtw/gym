import unittest

from reverse_string import reverse

class TestBasicFunctionality(unittest.TestCase):
    def test_reverse(self):
        r = reverse(["a", "b", "c"])
        self.assertEqual(["c","b","a"], r)