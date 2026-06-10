from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"],
    "E": ["F"],
    "F": ["E"]
}

visited = set()
stack = ["A"]
queue = deque(["A"])


def visit_all_bfs():
    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        print(node)

        for n in graph[node]:
            queue.append(n)
            

def visit_all_dfs():

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        print(node)

        for n in graph[node]:
            stack.append(n)

# def dfs(node):
#     if node in visited:
#         return
#
#     visited.add(node)
#
#     print(node)
#
#     for neighbor in graph[node]:
#         dfs(neighbor)

