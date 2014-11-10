from unittest import TestCase
from algos.heap_stack import HeapStack

class TestHeapStack(TestCase):

	def test_should_get_two_max_numbers(self):
		a = [3, 5, 8, 2, 9, 1]

		stack = HeapStack()
		stack.push_all(a)

		self.assertEquals(9, stack.find(0))
		self.assertEquals(8, stack.find(1))


	def test_should_get_kth_element(self):
		a = [3, 5, 8, 2, 9, 1]
		stack = HeapStack()
		stack.push_all(a)

		self.assertEquals(5, stack.find(2))

	def test_should_reorganing_max_after_being_removed(self):
		a = [3, 5, 8, 2, 1, 9]
		stack = HeapStack()
		stack.push_all(a)

		self.assertEquals(9, stack.find(0))
		self.assertEquals(9, stack.top())

		stack.pop()

		self.assertEquals(8, stack.find(0))
		self.assertEquals(5, stack.find(1))


