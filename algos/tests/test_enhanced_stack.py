from unittest import TestCase
from algos.enhanced_stack import EnhancedStack


class TestEnhancedStack(TestCase):

	def setUp(self):
		self._stack = EnhancedStack()

	def test_should_get_minimum_in_O1(self):
		for i in range(10, -1, -1):
			self._stack.push(i)
			self.assertEquals(i, self._stack.find_min())


	def test_should_get_minimum_after_pops(self):
		self._stack.push(2)
		self._stack.push(1)

		self.assertEquals(1, self._stack.find_min())
		self._stack.pop()
		self.assertEquals(2, self._stack.find_min())


