from unittest import TestCase
from algos.duplications import remove_duplicates

class TestRemoveDuplicates(TestCase):

	def test_remove_duplicates_entries(self):
		a = ["dog", "cat", "cat", "bird", "bat", "dog"]

		self.assertEquals(["dog", "cat", "bird", "bat"], remove_duplicates(a))