from unittest import TestCase
from algos.pair_sum import PairSum

class TestSubSum(TestCase):

	def test_should_return_indexes_properly(self):
		a = [3, 4, 7, 1, 2, 9, 8]
		self.assertEquals([1, 6, 5, 0], PairSum(a).get_indexes())