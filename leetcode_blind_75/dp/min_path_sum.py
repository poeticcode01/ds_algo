from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[float('inf')]*col for i in range(row)]
        dp[row-1][col-1] = grid[row-1][col-1]

        i = row-2
        while i >= 0:
            dp[i][col-1] = grid[i][col-1] + dp[i+1][col-1]
            i -=1

        i = col-2
        while i >= 0:
            dp[row-1][i] = grid[row-1][i] + dp[row-1][i+1]
            i -=1

        cur_col = col-2
        while cur_col >= 0:
            cur_row = row-2
            while cur_row >= 0:
                dp[cur_row][cur_col] = grid[cur_row][cur_col] + min(dp[cur_row][cur_col+1],dp[cur_row+1][cur_col])
                cur_row -=1
            cur_col -=1
        
        return dp[0][0]
        
        