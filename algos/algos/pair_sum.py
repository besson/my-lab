class PairSum:

	def __init__(self, array):
		self._array = array

	def get_indexes(self):
		idx_map = self._get_idx_map();
		sum_map = {}
		solution = []

		for i, ival in enumerate(self._array):
			for j in range(i + 1, len(self._array)):
				jval = self._array[j]
				sum_map[ival + jval] = [i, j]

		for sum_key in sum_map.keys():
			for i_key in idx_map.keys():
				if ((sum_key - i_key) in idx_map.keys()):
					a = sum_map[sum_key][0]
					b = sum_map[sum_key][1]
					c = idx_map[i_key]
					d = idx_map[sum_key - i_key]

					cand_sol = [a, b, c, d]

					if (len(set(cand_sol)) == len(cand_sol)):
						solution = cand_sol

		return solution


	def _get_idx_map(self):
		result = {}

		for idx, val in enumerate(self._array):
			result[val] = idx

		return result
