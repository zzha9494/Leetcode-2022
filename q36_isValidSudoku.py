from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for i in range(9)]  # whether current number appeared in the i-th row
        column = [[False] * 9 for i in range(9)]
        box = [[False] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                curNum = ord(board[i][j]) - ord("1")
                if row[i][curNum] or column[j][curNum] or box[i // 3 + j // 3 * 3][curNum]:
                    return False
                row[i][curNum], column[j][curNum], box[i // 3 + j // 3 * 3][curNum] = True, True, True
        return True
