from unittest import TestCase
from algos.binary_search_lab import BinarySearchLab


class TestBinarySearchLab(TestCase):

    def test_simple_operation_on_simple_algo(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(BinarySearchLab().find(a, 5))

    def test_simple_operation_simple_algo_not_find(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(BinarySearchLab().find(a, 42))

    def test_simple_operation_on_rotated_array_find_one(self):
        a = [4, 5, 6, 7, 8, 1, 2, 3]
        self.assertTrue(BinarySearchLab().find_enhanced(a, 1))

    def test_simple_operation_on_rotated_array_find_5(self):
        a = [4, 5, 6, 7, 8, 1, 2, 3]
        self.assertTrue(BinarySearchLab().find_enhanced(a, 5))

    def test_simple_operation_rotate_array_not_find(self):
        a = [4, 5, 6, 7, 8, 1, 2, 3]
        self.assertTrue(BinarySearchLab().find_enhanced(a, 42))




