# https://leetcode.com/problems/valid-sudoku
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(lst):
            hash = set()
            for i in lst:
                if i != ".":
                    if i not in hash:
                        hash.add(i)
                    else:
                        return False
            return True

        for i in range(9):
            if not is_valid(board[i]):
                return False

        for j in range(9):
            col = []
            for i in range(9):
                col.append(board[i][j])
            if not is_valid(col):
                return False

        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                sub_box = []
                for i in range(a, a + 3):
                    for j in range(b, b + 3):
                        sub_box.append(board[i][j])
                if not is_valid(sub_box):
                    return False
        return True
