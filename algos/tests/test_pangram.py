from unittest import TestCase
from algos.pangram import is_valid

class TestPangram(TestCase):

	def test_should_detect_pangram(self):
		sentence = "We promptly judged antique ivory buckles for the next prize"
		self.assertTrue(is_valid(sentence))

	def test_should_not_detect_pangram(self):
		sentence = "We promptly judged antique ivory buckles for the prize"
		self.assertFalse(is_valid(sentence))	

	def test_should_detect_pangram_with_numbers(self):
		sentence = "We promptly judged antique ivory buckles for the prize 4 all 2"
		self.assertFalse(is_valid(sentence))		