from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return []

        n, m = len(image), len(image[0])
        original_pixel = image[sr][sc]

        def dfs(i, j):
            image[i][j] = color
            neighbors = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)
            ]

            for ni, nj in neighbors:
                if 0 <= ni < n and 0 <= nj < m:
                    current = image[ni][nj]
                    print(current)
                    if image[ni][nj] == original_pixel and image[ni][nj] != color:
                        image[ni][nj] = color
                        dfs(ni, nj)


        dfs(sr, sc)

        return image