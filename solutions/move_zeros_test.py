import unittest

from solutions.move_zeros import move_zeros


class TestBasicFunctionality(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual(move_zeros([0,1,0,2,3]), [1,2,3,0,0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([0,1]), [1,0])
        self.assertEqual(move_zeros([1,1]), [1,1])
        self.assertEqual(move_zeros([1,1,0]), [1,1,0])

