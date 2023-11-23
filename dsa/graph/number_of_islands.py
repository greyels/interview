from typing import List


class Solution:
    # BFS
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    queue = [(i, j)]
                    grid[i][j] = '2'
                    while queue:
                        row, col = queue.pop()
                        for step_r, step_c in (0, 1), (1, 0), (-1, 0), (0, -1):
                            cord_r = row + step_r
                            cord_c = col + step_c
                            if 0 <= cord_r < rows and 0 <= cord_c < cols:
                                if grid[cord_r][cord_c] == '1':
                                    grid[cord_r][cord_c] = '2'
                                    queue.append((cord_r, cord_c))
                    num += 1
        return num

    # DFS
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = '2'
            dirs = (0, 1), (1, 0), (-1, 0), (0, -1)
            for step_r, step_c in dirs:
                cord_r = row + step_r
                cord_c = col + step_c
                if 0 <= cord_r < rows and 0 <= cord_c < cols:
                    if grid[cord_r][cord_c] == '1':
                        dfs(cord_r, cord_c)

        rows = len(grid)
        cols = len(grid[0])
        num = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num += 1
        return num
