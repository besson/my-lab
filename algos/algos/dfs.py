class DFS:

    def __init__(self, graph):
        self._graph = graph

    def find(self, origin, node):
        visited = {}
        nodes = []
        nodes.append(origin)

        while len(nodes) > 0:
            current_node = nodes.pop()

            if current_node not in visited:
                visited[current_node] = 1
                neighbors = self._graph[current_node]

                for n in neighbors:
                    if n in visited:
                        continue

                    if n == node:
                        return True

                    nodes.append(n)

        return False
