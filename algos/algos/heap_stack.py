class HeapStack:

	def __init__(self):
		self._sorted = []
		self._stack = []
		self._map = []

	def push_all(self, array):
		for el in array:
			self._stack.insert(0, el)
			self._sorted.append(el)

		self._sorted = sorted(self._sorted, reverse=True)
		self._create_map()

	def find(self, position):
		return self._sorted[position]

	def pop(self):
		popped = self._stack.pop(0)
		i = self._map[popped]
		self._sorted.pop(i)

		return popped

	def push(self, val):
		self._sorted.insert(0, val)
		self._sorted = sorted(self._sorted, reverse=True)
		self._create_map()

	def top(self):
		return self._stack[0]

	def _create_map(self):
		self._map = {}
		for i, val in enumerate(self._sorted):
			self._map[val] = i


