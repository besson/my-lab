from unittest import TestCase
from algos.anagram_count import count

class TestAnagramCount(TestCase):

	def test_contains_2_anagrams(self):
		a = ["count", "dog", "cat", "act"]
		self.assertEquals({"count": 1, "dog": 1, "cat": 2, "act": 2}, count(a))