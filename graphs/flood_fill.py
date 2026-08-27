from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return []

        n, m = len(image), len(image[0])

        def dfs(i, j):
            neighbors = [(
                i + 1, j,
                i - 1, j,
                i, j + 1,
                i, j - 1
            )]

            for ni, nj in neighbors:
                if 0 <= ni < n and 0 <= nj < m and image[ni][nj] != color:
                    image[ni][nj] = color
                    dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                dfs(i, j)

        return image