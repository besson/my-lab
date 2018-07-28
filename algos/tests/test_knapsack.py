from unittest import TestCase
from algos.knapsack import Knapsack


class TestKnapsack(TestCase):

    def test_should_return_max_value_1(self):
      values = [20, 5, 10, 40, 15, 25]
      weights = [1, 2, 3, 8, 7, 4]
      w = 10

      self.assertEqual(200, Knapsack(values, weights, w).calculate_with_repetition())

    def test_should_return_max_value_1(self):
        values = [20, 5, 10, 40, 15, 25]
        weights = [1, 2, 3, 8, 7, 4]
        w = 10

        self.assertEqual(60, Knapsack(values, weights, w).calculate())
