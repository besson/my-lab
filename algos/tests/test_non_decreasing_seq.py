from unittest import TestCase
from algos.non_decreasing_seq import NonDecreasingSeq


class TestNonDecreasingSeq(TestCase):

    def test_single_seq(self):
        self.assertEquals(1, NonDecreasingSeq().get_seq([1]))

    def test_array_with_one_seq(self):
        self.assertEquals(3, NonDecreasingSeq().get_seq([1, 4, 3, 5]))

    def test_array_with_a_more_complex_seq(self):
        self.assertEquals(4, NonDecreasingSeq().get_seq([5, 3, 4, 8, 6, 7]))

    def test_array_with_a_bigger_seq(self):
        self.assertEquals(7, NonDecreasingSeq().get_seq([5, 3, 4, 8, 6, 7, 5, 4, 11, 12, 13]))