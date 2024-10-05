from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        cur_row = 0
        cur_col = col - 1

        while cur_row >= 0 and cur_row < row and cur_col >= 0 and cur_col < col:
            if matrix[cur_row][cur_col] == target:
                return True

            elif matrix[cur_row][cur_col] > target:
                cur_col -=1
            else:
                cur_row +=1

        return False