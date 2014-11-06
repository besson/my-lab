from unittest import TestCase
from algos.fibonacci_sum import FibonacciSum

class TestFibonacciSum(TestCase):

	def test_return_2_numbers_as_minimum(self):
		fibonacci = FibonacciSum(7)
		self.assertEquals(2, fibonacci.count())

	def test_return_3_numbers_as_minimum(self):
		fibonacci = FibonacciSum(70)
		self.assertEquals(3, fibonacci.count())

	def test_return_1_numbers_as_minimum(self):
		fibonacci = FibonacciSum(8)
		self.assertEquals(1, fibonacci.count())