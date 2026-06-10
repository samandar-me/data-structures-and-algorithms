trusts = [
    [1, 4],
    [2, 4],
    [3, 4],
]

def find_judge(n: int, trust) -> int:
    score = [0] * (n + 1)

    for a, b in trust:
        score[a] -= 1
        score[b] += 1

    for p in range(1, n + 1):
        if score[p] == n - 1:
            return p

    return -1

if __name__ == '__main__':
    print(find_judge(4, trusts))
