from unittest import TestCase
from algos.quick_sort import QuickSort


class TestQuickSort(TestCase):

    def test_partition_arrays(self):
        a = [4, 3, 5, 7, 2, 1, 6]
        new_pos = QuickSort(a).partition(a, 0, 6)

        self.assertEquals(3, new_pos)
        self.assertEquals([2, 3, 1, 4, 7, 5, 6], a)

    def test_partition_inline(self):
        a = [1, 3, 5, 7, 2, 4, 6]
        new_pos = QuickSort(a).partition(a, 2, 6)

        self.assertEquals(4, new_pos)
        self.assertEquals([1, 3, 2, 4, 5, 7, 6], a)

    def test_partition_almost_sorted_array(self):
        a = [1, 2, 3, 6, 5, 4, 7]
        new_pos = QuickSort(a).partition(a, 3, 5)
        self.assertEquals(5, new_pos)
        self.assertEquals([1, 2, 3, 4, 5, 6, 7], a)

    def test_sort_array(self):
        a = [1, 3, 5, 7, 2, 4, 6]
        QuickSort(a).sort()

        self.assertEquals([1, 2, 3, 4, 5, 6, 7], a)

    def test_totaly_unsort_array(self):
        a = [7, 6, 5, 4, 3, 2, 1]
        QuickSort(a).sort()

        self.assertEquals([1, 2, 3, 4, 5, 6, 7], a)