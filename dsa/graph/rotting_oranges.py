from typing import List


class Solution:
    # BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                if grid[row][col] == 1:
                    fresh_cnt += 1
        minutes = 0
        while rotten and fresh_cnt > 0:
            for _ in range(len(rotten)):
                row, col = rotten.pop(0)
                for dr, dc in (0, 1), (1, 0), (-1, 0), (0, -1):
                    new_r = row + dr
                    new_c = col + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            rotten.append((new_r, new_c))
                            fresh_cnt -= 1
            minutes += 1
        return minutes if fresh_cnt == 0 else -1
