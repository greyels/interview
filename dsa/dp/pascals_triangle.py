from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        if numRows == 2:
            return res
        for i in range(numRows - 2):
            new_row = [1]
            for j in range(len(res[-1]) - 1):
                new_row.append(res[-1][j] + res[-1][j + 1])
            new_row.append(1)
            res.append(new_row)
        return res


assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print("OK")
