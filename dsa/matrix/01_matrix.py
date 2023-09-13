from typing import List


class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.mat = None

    def check_next_cell(self, i, j, steps, visited):
        if self.mat[i][j] != 0:
            visited.add((i, j))
            steps_l = steps_b = steps_r = steps_t = 99999
            steps += 1
            if i > 0 and ((i - 1, j) not in visited):
                steps_l = self.check_next_cell(i - 1, j, steps, visited)
            if j > 0 and ((i, j - 1) not in visited):
                steps_b = self.check_next_cell(i, j - 1, steps, visited)
            if i < self.x and ((i + 1, j) not in visited):
                steps_r = self.check_next_cell(i + 1, j, steps, visited)
            if j < self.y and ((i, j + 1) not in visited):
                steps_t = self.check_next_cell(i, j + 1, steps, visited)
            steps = min(steps_l, steps_r, steps_b, steps_t)
        return steps

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.y = len(mat)
        self.x = len(mat[0])
        result = [[0 for i in range(self.x)] for i in range(self.y)]
        for i in range(self.x):
            for j in range(self.y):
                result[i][j] = self.check_next_cell(i, j, 0, set())
        return result


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
actual = Solution().updateMatrix(mat)
expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
assert actual == expected
print("OK")
