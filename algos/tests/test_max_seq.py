from unittest import TestCase
from algos.max_seq import MaxSeq


class TestMaxSeq(TestCase):

    def test_simple_get_max_seq(self):
        a = [4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18, 20, 22, 23, 24, 27]
        seq = MaxSeq(a)
        seq.run()

        self.assertEquals(seq.start(), 0)
        self.assertEquals(seq.end(), 5)