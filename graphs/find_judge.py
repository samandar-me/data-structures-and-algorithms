from collections import Counter

def find_judge(n: int, trust: list) -> int:
    people = list(range(1, n + 1))
    indegree = Counter()
    outdegree = Counter()

    for a, b in trust:
        indegree[b] += 1
        outdegree[a] += 1

    for person in people:
        if indegree[person] == n - 1 and outdegree[person] == 0:
            return person

    return -1

