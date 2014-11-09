class Sum3Zero:

	def __init__(self, array):
		self._array = array

	def find(self):
		negatives = {}
		diffs = {}

		for i, val in enumerate(self._array):
			if (val < 0):
				negatives[self._array.pop(i)] = 1

		for i, val in enumerate(self._array):
			if (val in diffs.keys()):
				numbers = diffs[val]
				numbers.append(val)
				return numbers

			else:
				for key in negatives.keys():
					numbers = [key, val]
					diffs[abs(key + val)] = numbers

		return []