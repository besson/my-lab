# A stack which the operations Push, Pop and Find Minimum can be done in O(1) 
# PS: Space is not a contraint

class EnhancedStack:

	def __init__(self):
		self._min_elements = []
		self._stack = []


	def push(self, elem):
		self._stack.insert(0, elem)

		if (len(self._min_elements) > 0):
			if (elem <= self._min_elements[0]):
				self._min_elements.insert(0, elem)
		else:
			self._min_elements.insert(0, elem)

	def pop(self):
		if (self._stack[0] == self._min_elements[0]):
			self._min_elements.pop(0)

		return self._stack.pop(0)

	def find_min(self):
		return self._min_elements[0]
		