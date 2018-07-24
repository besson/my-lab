from unittest import TestCase
from algos.dfs import DFS


class TestDFS(TestCase):

    def setUp(self):
        self._graph = {
            'S': ['A', 'C'],
            'A': ['S', 'D'],
            'D': ['A', 'G'],
            'G': ['D', 'F', 'E'],
            'E': ['G', 'B'],
            'B': ['E', 'S'],
            'F': ['G', 'C'],
            'C': ['F', 'S']
        }

    def test_return_the_only_node_tree(self):
        graph = {'A': []}
        self.assertEqual(False, DFS(graph).find('A', 'A'))

    def test_return_value_1(self):
        self.assertEqual(True, DFS(self._graph).find('S', 'A'))

    def test_return_value_2(self):
        self.assertEqual(True, DFS(self._graph).find('S', 'B'))

    def test_return_value_3(self):
        self.assertEqual(True, DFS(self._graph).find('G', 'A'))

    def test_no_return_value_1(self):
        self.assertEqual(False, DFS(self._graph).find('S', 'Z'))

