from unittest import TestCase
from algos.binary_search_lab import BinarySearchLab


class TestBinarySearchLab(TestCase):

    def test_simple_operation_on_simple_algo(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(BinarySearchLab().find(a, 5))