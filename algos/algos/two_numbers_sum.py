# find two elements in array where its sum is closest to zero

from merge_sort import sort
import sys

class TwoNumbersSum:

	def __init__(self, array):
		self._array = array
		self._neg = {}

	def closest_to_zero(self):
		self._map_negatives()
		abs_array = [abs(self._array[x]) for x in range(len(self._array))]
		sa = sort(abs_array)

		min_dist = sys.maxint
		a1 = 0
		a2 = 0

		for i in range(len(sa)):
			if (sa[i] in self._neg.keys()):
				self._neg[sa[i]] = self._neg[sa[i]] - 1
				sa[i] = -1 * sa[i]

			if ((i + 1) < len(sa) and abs(sa[i] + sa[i + 1]) <= min_dist):
				if (abs(sa[i]) in self._neg.keys() and self._neg[abs(sa[i])] == 0):
					min_dist = abs(sa[i] + sa[i + 1])
					a1 = sa[i]
					a2 = sa[i + 1]

			if ((i - 1) >= 0 and abs(sa[i] + sa[i - 1]) <= min_dist):
				min_dist = abs(sa[i] + sa[i - 1])
				a1 = sa[i]
				a2 = sa[i - 1]

		return (a1, a2)

	def _map_negatives(self):
		for i in range(len(self._array)):
			elem = self._array[i] 
			if (elem < 0):
				if (abs(elem) in self._neg):
					self._neg[abs(elem)] = self._neg[abs(elem)] + 1
				else:
					self._neg[abs(elem)] = 1



