import math


class Dijkstra():

    def __init__(self, graph):
        self.__graph = graph

    def find_min_distance(self, node1, node2):
        if node1 == node2:
            return 0

        unvisited = list(self.__graph.keys())
        costs = self.build_node_costs(node1, unvisited)
        current_node = node1
        min_node = current_node

        while len(unvisited) > 0:
            nodes = self.__graph[current_node]
            min_distance = math.inf

            for node in nodes:
                key = self.get_key(node)
                distance = node[key]

                if key not in unvisited:
                    continue

                if distance + costs[current_node] < costs[key]:
                    costs[key] = distance + costs[current_node]

                if costs[key] < min_distance:
                    min_node = key
                    min_distance = costs[key]

            if unvisited.index(current_node) != -1:
                unvisited.pop(unvisited.index(current_node))

                if current_node == node2:
                    return costs[current_node]

            if current_node == min_node and len(unvisited) > 0:
                min_node = unvisited[0]

            current_node = min_node

        return -1

    def build_node_costs(self, node1, unvisited):
        costs = {}
        for k in unvisited:
            costs[k] = math.inf
        costs[node1] = 0
        return costs

    def get_key(self, node):
        return list(node.keys())[0]







