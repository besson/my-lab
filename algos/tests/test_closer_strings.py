from unittest import TestCase
from algos.closer_strings import are_closer

class TestCloserString(TestCase):

	def test_should_be_closer(self):
		self.assertTrue(are_closer("xyz", "xz"))		
		self.assertTrue(are_closer("xyz", "xyk"))
		self.assertTrue(are_closer("xy", "xyz"))

	def test_should_not_be_closer(self):
		self.assertFalse(are_closer("xyz", "xyz"))
		self.assertFalse(are_closer("xyz", "xzy"))
		self.assertFalse(are_closer("x", "xyz"))