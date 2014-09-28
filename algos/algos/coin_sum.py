import sys


class CoinSum:

    def __init__(self, coins):
        self._coins = coins
        self._min = []

    def get_min_coins(self, _sum):
        self._init_min_sums(_sum + 1)

        for i in range(1, _sum + 1):
            for coin in self._coins:
                if (coin <= i and self._min[i - coin] + 1 < self._min[i]):
                    self._min[i] = self._min[i - coin] + 1

        return self._min[_sum]

    def _init_min_sums(self, _sum):
        self._min = [sys.maxint for i in range(0, _sum)]
        self._min[0] = 0