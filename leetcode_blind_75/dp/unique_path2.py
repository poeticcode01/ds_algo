from ast import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_cnt = len(obstacleGrid)
        col_cnt = len(obstacleGrid[0])

        dp =[[0]*col_cnt for i in range(row_cnt)]
        dp[row_cnt-1][col_cnt-1] = 1 if obstacleGrid[row_cnt-1][col_cnt-1] == 0 else 0

        i = row_cnt-2
        while i >= 0:
            if obstacleGrid[i][col_cnt-1] == 1:
                i -=1
                continue
            dp[i][col_cnt-1] = dp[i+1][col_cnt-1]
            i -=1
        
        i = col_cnt-2
        while i >= 0:
            if obstacleGrid[row_cnt-1][i] == 1:
                i -=1
                continue
            dp[row_cnt-1][i] = dp[row_cnt-1][i+1]
            i -=1

        i = col_cnt-2
        while i >= 0:
            j = row_cnt-2
            while j >= 0:
                if obstacleGrid[j][i] == 1:
                    j -=1
                    continue
                dp[j][i] = dp[j+1][i]+dp[j][i+1]
                j -=1
            i -=1
        
        return dp[0][0]