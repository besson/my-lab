from unittes import TestCase
from algos.array_matching import ArrayMatching

class TestArrayMatching(TestCase):

	def test_should_match_A_with_all_B(self):
		a = [3, 5, 2, 4, 1]
		b = [1, 3, 2, 5, 4]

		result = {0:1, 1:3, 2:2, 3:4, 4:0}

		self.assertEquals(result, ArrayMatching(a, b).match())

