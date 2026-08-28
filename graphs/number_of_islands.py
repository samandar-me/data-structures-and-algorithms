WATER = "0"
LAND = "1"

def num_islands(matrix: list) -> int:
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    visited = set()

    def dfs(i, j):
        visited.add((i, j))
        neighbors = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ]

        for ni, nj in neighbors:
            if (ni, nj) in visited: continue
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == LAND:
                dfs(ni, nj)

    lands = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == LAND and (i, j) not in visited:
                dfs(i, j)
                lands+=1

    return lands