from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbour in graph[node]:
                stack.append(neighbour)
                if neighbour == destination:
                    return True

        return False