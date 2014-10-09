from unittest import TestCase
from algos.merge_sort import merge, sort


class TestMergeSort(TestCase):

    def test_merge_two_arrays(self):
        a = [1, 3, 5, 7]
        b = [2, 4, 6]

        self.assertEquals([1, 2, 3, 4, 5, 6, 7], merge(a, b))

    def test_sort_array(self):
        a = [7, 4, 1, 3, 6, 5, 2]

        self.assertEquals([1, 2, 3, 4, 5, 6, 7], sort(a))