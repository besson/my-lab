from unittest import TestCase
from algos.string_combinations import StringCombinations

class TestStringCombinations(TestCase):

	def test_simple_combination(self):
		_input = [["quick", "slow"], ["brown", "red"], ["fox", "dog"]] 
		_output = ["quick brown fox", 
					"quick brown dog",
					"quick red fox",
					"quick red dog",
					"slow brown fox",
					"slow brown dog",
					"slow red fox",
					"slow red dog"]

		self.assertEquals(_output, StringCombinations(_input).print_all())