from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = row - 1
        k = 0
        l = col - 1
        ans = []
        while i <= j and k <= l:
            cur_col = k
            while cur_col <= l:
                ans.append(matrix[i][cur_col])
                cur_col +=1
            i +=1
            if i > j:
                break
            cur_row = i
            while cur_row <= j:
                ans.append(matrix[cur_row][l])
                cur_row +=1
            l -=1
            if k > l:
                break
            cur_col = l
            while cur_col >= k:
                ans.append(matrix[j][cur_col])
                cur_col -=1
            j -=1
            if i > j:
                break
            cur_row = j
            while cur_row >= i:
                ans.append(matrix[cur_row][k])
                cur_row -=1
            k +=1
        return ans