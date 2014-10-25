from unittest import TestCase
from algos.flip_zeros import get_flip_positions


class FlipZerosTest(TestCase):

    def test_get_flip_on_position_2(self):
        a = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        # number of allowed flips
        m = 1

        self.assertEquals([2], get_flip_positions(a, m))

    def test_get_flips_correctly(self):
        a = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
        m = 2

        self.assertEquals([5, 6], get_flip_positions(a, m))