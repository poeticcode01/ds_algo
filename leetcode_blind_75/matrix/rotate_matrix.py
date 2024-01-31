from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for cur_col in range(col):
            i = 0
            j = row - 1
            while i < j:
                matrix[i][cur_col],matrix[j][cur_col] = matrix[j][cur_col],matrix[i][cur_col]
                i +=1
                j -=1
        # print(matrix)  
        for cur_row in range(row):
            cur_col = cur_row + 1
            while cur_col < col:
                matrix[cur_row][cur_col],matrix[cur_col][cur_row] = matrix[cur_col][cur_row],matrix[cur_row][cur_col]
                cur_col +=1