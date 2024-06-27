from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        is_first_col = False
        for i in range(row):
            if matrix[i][0] == 0:
                is_first_col = True
                break

        for i in range(row):
            for j in range(1,col):
                # if j == 0:
                #     continue

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,col):
            if matrix[0][i] == 0:
                for j in range(row):
                    matrix[j][i] = 0

        for i in range(row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0

        if is_first_col:
            for i in range(row):
                matrix[i][0] = 0
































# from typing import List


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = len(matrix)
#         col = len(matrix[0])
#         identifier = -(2**31)-1
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == 0:
#                     for k in range(col):
#                         if matrix[i][k] == 0:
#                             matrix[i][k] = identifier
#                         else:
#                             matrix[i][k] = 0
#                     break

#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == identifier:
#                     for k in range(row):
#                         matrix[k][j] = 0