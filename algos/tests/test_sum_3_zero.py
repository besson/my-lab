from unittest import TestCase
from algos.sum_3_zero import Sum3Zero

class TestSum3Zero(TestCase):

	def test_simple_case_with_one_negative(self):
		a = [-5, 1, 2, 3, 9]
		self.assertEquals([-5, 2, 3], Sum3Zero(a).find())