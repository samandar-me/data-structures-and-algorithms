from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_vertical = [[0] * rows for _ in range(cols)]
        output = 0

        for col in range(cols):
            for row in range(rows):
                grid_vertical[col][row] = grid[row][col]

        grid_vertical_map = {}

        for i in range(len(grid_vertical)):
            key = tuple(grid_vertical[i])
            current_count = grid_vertical_map.get(key, 0)
            grid_vertical_map[key] = current_count + 1

        for row in range(rows):
            sgrid = tuple(grid[row])
            if sgrid in grid_vertical_map:
                output += grid_vertical_map.get(sgrid, 0)

        return output
