from unittest import TestCase
from algos.anagram_counter import AnagramCounter

class TestAnagramCount(TestCase):

	def test_contains_2_anagrams(self):
		a = ["count", "dog", "cat", "act"]
		self.assertEquals({"count": 1, "dog": 1, "cat": 2, "act": 2}, AnagramCounter(a).count())

	def test_contains_3_anagrams(self):
		a = ["count", "dog", "cat", "act", "tac"]
		self.assertEquals({"count": 1, "dog": 1, "cat": 3, "act": 3, "tac": 3}, AnagramCounter(a).count())