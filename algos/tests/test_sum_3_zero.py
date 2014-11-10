from unittest import TestCase
from algos.sum_3_zero import Sum3Zero

class TestSum3Zero(TestCase):

	def test_simple_case_with_one_negative(self):
		a = [-5, 1, 2, 3, 9]
		self.assertEquals([-5, 2, 3], Sum3Zero(a).find())

	def test_simple_case_with_more_negatives(self):
		a = [-5, 1, 2, 3, 9, -2, -15, -18]
		self.assertEquals([-5, 2, 3], Sum3Zero(a).find())	

	def test_simple_case_with_no_solution(self):
		a = [-5, 1, -2, 30]
		self.assertEquals([], Sum3Zero(a).find())		