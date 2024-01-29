from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        identifier = -(2**31)-1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(col):
                        if matrix[i][k] == 0:
                            matrix[i][k] = identifier
                        else:
                            matrix[i][k] = 0
                    break

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == identifier:
                    for k in range(row):
                        matrix[k][j] = 0