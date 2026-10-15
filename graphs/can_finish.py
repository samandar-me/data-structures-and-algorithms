from collections import defaultdict

def canFinish(n: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    visited = set()

    for u, v in prerequisites:
        graph[u].append(v)

    def dfs(i, visiting):
        if i in visited:
            raise ValueError("cycle detected")

        visiting.add(i)

        for ni in graph[i]:
            dfs(ni, visiting)

        visited.add(i)

    for i in range(n):
        if i in visited: continue
        try:
            dfs(i, set())
        except ValueError:
            return False

    return True