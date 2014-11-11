from unittest import TestCase

class BinarySum(TestCase):

	def test_should_sum_simple_numbers(self):
		a = "100"
		b = "101"

		self.assertEquals("1001", sum(a,b))

	def test_should_more_complex_numbers(self):
		a = "1111"
		b = "0011"

		self.assertEquals("10001", sum(a,b))	