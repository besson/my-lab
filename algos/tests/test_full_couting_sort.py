from unittest import TestCase

class TestFullCountingSort(TestCase):

	def test_should_print_strings_in_initial_order(self):
		actual = get_strings_in_order(20, "data/count_list_1.txt")
		expected = "- - - - - to be or not to be - that is the question - - - -"

		self.assertEquals(expected, actual)