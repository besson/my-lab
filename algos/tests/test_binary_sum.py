from unittest import TestCase
from algos.binary_sum import sum_bin

class BinarySum(TestCase):

	def test_should_sum_simple_numbers(self):
		a = "100"
		b = "101"

		self.assertEquals("1001", sum_bin(a, b))

	def test_should_more_complex_numbers(self):
		a = "1111"
		b = "0011"

		self.assertEquals("10010", sum_bin(a, b))	

	def test_should_more_two_equal_numbers(self):
		a = "11"
		b = "11"

		self.assertEquals("110", sum_bin(a, b))		