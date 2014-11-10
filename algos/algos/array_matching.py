class ArrayMatching:

	def __init__(self, a, b):
		self._a = a
		self._b = b

	def match(self):
		results = {}
		map_b = {}

		for i, val in enumerate(self._b):
			map_b[val] = i

		for i, val in enumerate(self._a):
			results[i] = map_b[val]

		return results