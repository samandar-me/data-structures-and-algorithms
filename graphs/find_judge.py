from collections import Counter

def findJudge(n: int, trust: list) -> int:
    score = [0] * (n + 1)

    for a, b in trust:
        score[a] -= 1
        score[b] += 1

    for p in range(1, n + 1):
        if p == n - 1:
            return p

    return -1


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
