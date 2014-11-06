# How many minium numbers from fibonacci series are required such the sum of these numbers is equal to given N

import sys

class FibonacciSum:

	def __init__(self, target):
		self._target = target
		self._fibo_numbers = self._get_fibo_numbers(target)
		self._min = []
		self._build_min_array(target)

	def count(self):
		for i in range(0, self._target + 1):
			for j in self._fibo_numbers:
				if (j <= i and self._min[i - j] + 1 <= self._min[i]):
					self._min[i] = self._min[i - j] + 1

		return self._min[self._target]

	def _get_fibo_numbers(self, target):
		fibo = [1, 1]

		for i in range(2, target + 1):
			if (i - 1 <= len(fibo) - 1):
				number = fibo[i - 1] + fibo[i - 2]

				if (number <= target):
					fibo.append(number)

		return fibo

	def _build_min_array(self, target):
		self._min = [sys.maxint for x in range(0,target + 1)]
		self._min[0] = 0
