from unittest import TestCase
from algos.dijkstra import Dijkstra


class TestDijkstra(TestCase):

    def setUp(self):
        self._graph = {
            'A': [{'B': 2}, {'C': 3}],
            'B': [{'D': 1}, {'E': 3}],
            'C': [{'E': 1}],
            'D': [{'F': 1}],
            'E': [{'F': 1}],
            'F': []
        }

    def test_return_zero_when_graph_is_only_one_node(self):
        graph = {'A': []}
        self.assertEqual(0, Dijkstra(graph).find_min_distance('A', 'A'))

    def test_return_min_distance_1(self):
        self.assertEqual(4, Dijkstra(self._graph).find_min_distance('A', 'E'))

    def test_return_min_distance_2(self):
        self.assertEqual(3, Dijkstra(self._graph).find_min_distance('A', 'D'))

    def test_return_min_distance_2(self):
        self.assertEqual(4, Dijkstra(self._graph).find_min_distance('A', 'F'))

    def test_no_route(self):
        self.assertEqual(-1, Dijkstra(self._graph).find_min_distance('A', 'H'))

