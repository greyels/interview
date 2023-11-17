from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(mat)
        cols = len(mat[0])
        queue = []
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = rows * cols
        while queue:
            row, col = queue.pop(0)
            for r, c in steps:
                r_step = row + r
                c_step = col + c
                if 0 <= r_step < rows and 0 <= c_step < cols and mat[r_step][c_step] == rows * cols:
                    mat[r_step][c_step] = mat[row][col] + 1
                    queue.append((r_step, c_step))
        return mat
