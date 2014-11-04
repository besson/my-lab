from unittest import TestCase
from algos.redundant_braces import has_redundant_braces

class TestRedundantBraces:

	def test_should_detect_redundant_braces(self):
		a = "((a+b))"
		self.assertTrue(has_redundant_braces(a))

	def test_should_not_detect_redundant_braces(self):
		a = "(a+(b+c))"
		self.assertFalse(has_redundant_braces(a))
