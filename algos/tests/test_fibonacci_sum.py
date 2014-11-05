from unittest import TestCase
from algos.fibonacci_sum import FibonacciSum

class TestFibonacciSum(TestCase):

	def setUp(self):
		self._fibonacci = FibonacciSum()

	def test_return_2_numbers_as_minimum(self):
		self.assertEquals(2, self._fibonacci.count(7))

	def test_return_3_numbers_as_minimum(self):
		self.assertEquals(3, self._fibonacci.count(70))

	def test_return_1_numbers_as_minimum(self):
		self.assertEquals(1, self._fibonacci.count(8))