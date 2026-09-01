from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        m, n = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        num_minutes = -1
        while queue:
            q_size = len(queue)
            num_minutes += 1

            for _ in range(q_size):
                i, j = queue.popleft()
                neighbor = [
                    (i, j + 1),
                    (i, j - 1),
                    (i + 1, j),
                    (i - 1, j),
                ]
                for r, c in neighbor:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        num_fresh -= 1
                        queue.append((r, c))

        if num_fresh == 0:
            return num_minutes

        return -1