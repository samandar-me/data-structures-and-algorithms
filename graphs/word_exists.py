from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        possible_cells = []
        m, n = len(board), len(board[0])
        word_size = len(word)
        visited = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    possible_cells.append((i, j))

        def dfs(i, j, index: int) -> int:
            visited.add((i, j))

            if board[i][j] != word[index]:
                return False

            index += 1

            if index == word_size:
                return True

            neighbor = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j -1),
            ]

            for r, c in neighbor:
                if (r, c) in visited: continue
                if 0 <= r < m and 0 <= c < n and index < word_size and board[r][c] == word[index]:
                    if dfs(r, c, index):
                        return True

            visited.remove((i, j))

            return False

        for i, j in possible_cells:
            visited = set()

            if dfs(i, j, 0):
                return True

        return False