from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = []
        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(grid[i][j])
            dp.append(temp)

        # print(dp)
        cur_col = col - 1
        while cur_col >= 0:
            cur_row = row - 1
            while cur_row >= 0:
                right = float('inf')
                down = float('inf')
                if cur_col + 1 < col:
                    right = dp[cur_row][cur_col+1]
                if cur_row + 1 < row:
                    down = dp[cur_row+1][cur_col]
                if right == down and right == float('inf'):
                    cur_row -=1
                    continue
                dp[cur_row][cur_col] = min(right,down) + dp[cur_row][cur_col]
                cur_row -=1
            cur_col -=1
        # print(dp)
        return dp[0][0]