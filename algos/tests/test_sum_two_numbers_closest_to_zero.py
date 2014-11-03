from unittest import TestCase
from algos.two_numbers_sum import TwoNumbersSum


class SumTwoNumberClosestToZero(TestCase):

    def test_simple_opposite_numbers(self):
        numbers = [-2, 3, 4, 5, 2, 10]
        self.assertEquals((-2, 2), TwoNumbersSum(numbers).closest_to_zero())

    def test_simple_closer_opposite_numbers(self):
        numbers = [-2, 2, 4, 5, 3, 10]
        self.assertEquals((-2, 2), TwoNumbersSum(numbers).closest_to_zero())

    def test_simple_different_numbers(self):
        numbers = [3, 18, 7, 2]
        self.assertEquals((3, 2), TwoNumbersSum(numbers).closest_to_zero())

    def test_simple_distant_numbers(self):
        numbers = [100, 2, -101, 7]
        self.assertEquals((-101, 100), TwoNumbersSum(numbers).closest_to_zero())

    def test_arrays_with_more_negative_numbers(self):
        numbers = [-2, -1, 0, 2, 3, 4, -10]
        self.assertEquals((-2, 2), TwoNumbersSum(numbers).closest_to_zero())