from unittest import TestCase
from algos.quick_sort import QuickSort


class TestQuickSort(TestCase):

    def test_partition_arrays(self):
        a = [4, 3, 5, 7, 2, 1, 6]
        new_pos = QuickSort(a).partition(0, 6)

        self.assertEquals(3, new_pos)
        self.assertEquals([2, 3, 1, 4, 7, 5, 6], a)

    def test_partition_inline(self):
        a = [1, 3, 5, 7, 2, 4, 6]
        new_pos = QuickSort(a).partition(2, 6)

        self.assertEquals(4, new_pos)
        self.assertEquals([1, 3, 2, 4, 5, 7, 6], a)

    def test_sort_array(self):
        a = [1, 3, 5, 7, 2, 4, 6]
        QuickSort(a).sort()

        self.assertEquals([1, 2, 3, 4, 5, 6, 7], a)