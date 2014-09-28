from unittest import TestCase
from algos.coin_sum import CoinSum


class TestCoinsSum(TestCase):

    def test_simplest_sum(self):
        coins = [1, 3, 5]
        self.assertEquals(0, CoinSum(coins).get_min_coins(0))

    def test_simple_sum_1(self):
        coins = [1, 3, 5]
        self.assertEquals(1, CoinSum(coins).get_min_coins(3))

    def test_simple_sum_2(self):
        coins = [1, 3, 5]
        self.assertEquals(2, CoinSum(coins).get_min_coins(4))

    def test_simple_sum_3(self):
        coins = [1, 3, 5]
        self.assertEquals(3, CoinSum(coins).get_min_coins(11))

    def test_simple_sum_4(self):
        coins = [1, 3, 5, 11]
        self.assertEquals(1, CoinSum(coins).get_min_coins(11))

    def test_simple_sum_5(self):
        coins = [1]
        self.assertEquals(42, CoinSum(coins).get_min_coins(42))