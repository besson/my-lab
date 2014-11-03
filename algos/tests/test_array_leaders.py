from unittest import TestCase
from algos.array_leaders import find_leaders

class TestArrayLeaders(TestCase):
	
	def test_find_3_leaders(self):
		a = [13, 17, 5, 4, 6, 2]
		self.assertEquals([17, 6, 2], find_leaders(a))

	def test_everbody_is_leader(self):
		a = [42, 42, 42]
		self.assertEquals([42, 42, 42], find_leaders(a))	