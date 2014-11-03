from unittest import TestCase
from algos.move_non_zeros import move_and_count

class TestMoveNonZeros(TestCase):

	def test_move_4_non_zeros_to_the_left(self):
		a = [1, 0, 2, 0, 0, 3, 4]

		self.assertEquals(4, move_and_count(a))
		self.assertEquals([1, 4, 2, 3, 0, 0, 0], a)


	def test_count_6_non_zero_to_the_left(self):
		a = [1, 4, 2, 6, 0, 3, 4]
		
		self.assertEquals(6, move_and_count(a))
		self.assertEquals([1, 4, 2, 6, 4, 3, 0], a)
