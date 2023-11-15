from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check_island(row, col):
            directions = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
            ]
            borders = 0
            for row_d, col_d in directions:
                adj_row = row + row_d
                adj_col = col + col_d
                if adj_row < 0 or adj_col < 0 or adj_row == len(grid) or adj_col == len(grid[0]):
                    borders += 1
                elif grid[adj_row][adj_col] == 0:
                    borders += 1
            return borders

        # rows -> len(grid)
        # cols -> len(grid[0])
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if it's an island
                if grid[row][col] == 1:
                    perimeter += check_island(row, col)
        return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
assert Solution().islandPerimeter(grid) == 16
print("OK")
