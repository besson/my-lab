class BFS:

    def __init__(self, graph):
        self._graph = graph

    def find(self, origin, node):
        queue = []
        visited = {}

        queue.insert(0, origin)

        while len(queue) > 0:
            current_node = queue.pop()
            visited[current_node] = 1

            for n in self._graph[current_node]:
                if n in visited:
                    continue

                if n == node:
                    return True

                queue.insert(0, n)

        return False
