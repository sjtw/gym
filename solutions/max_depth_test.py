import unittest

from max_profit import max_profit
from solutions.max_depth import TreeNode, max_depth


class TestBasicFunctionality(unittest.TestCase):
    def test_max_depth(self):
        t = TreeNode(3)
        t.left = TreeNode(9)
        t.right = TreeNode(20)
        t.right.left = TreeNode(15)
        t.right.right = TreeNode(7)

        self.assertEqual(max_depth(t), 3)