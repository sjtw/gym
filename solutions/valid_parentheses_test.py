import unittest

from solutions.valid_parentheses import valid_parentheses


class TestBasicFunctionality(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertTrue(valid_parentheses('()(){}{}[][]'),)
        self.assertTrue(valid_parentheses('({[]})'))
        self.assertTrue(valid_parentheses('[{}]'))
        self.assertFalse(valid_parentheses('{'))
        self.assertFalse(valid_parentheses('}'))
        self.assertFalse(valid_parentheses('('))
        self.assertFalse(valid_parentheses('{'))
        self.assertFalse(valid_parentheses(')(){}'))
        self.assertFalse(valid_parentheses('[{]}'))
