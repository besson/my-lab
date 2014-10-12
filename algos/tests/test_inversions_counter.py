from unittest import TestCase
from algos.counters import Counters


class TestInversionsCounter(TestCase):

    def test_counter_three_inversions(self):
        a = [1, 2, 3, 7, 4, 5, 6]
        self.assertEquals(3, Counters(a).count_inversions())

    def test_counter_no_inversions(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        self.assertEquals(0, Counters(a).count_inversions())

    def test_counter_one_inversions(self):
        a = [1, 2, 3, 4, 5, 7, 6]
        self.assertEquals(1, Counters(a).count_inversions())
