import unittest

from add_two_numbers import ListNode, add_two_numbers

class TestBasicFunctionality(unittest.TestCase):
    def test_add_two_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))  # 342
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        a = add_two_numbers(l1, l2)
        self.assertEqual(a.val, 7)
        self.assertEqual(a.next.val, 0)
        self.assertEqual(a.next.next.val, 8)
        self.assertEqual(a.next.next.next, None)
