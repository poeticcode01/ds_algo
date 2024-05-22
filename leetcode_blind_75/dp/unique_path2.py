from ast import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        for i in range(row):
            temp = []
            for j in range(col):
                temp.append(0)
            dp.append(temp)

        cur_col = col - 1
        while cur_col >= 0:
            cur_row = row - 1
            while cur_row >= 0:
                rt = 0
                down = 0
                if cur_col + 1 < col:
                    if obstacleGrid[cur_row][cur_col + 1] == 0:
                        rt = dp[cur_row][cur_col + 1]
                if cur_row + 1 < row:
                    if obstacleGrid[cur_row+1][cur_col] == 0:
                        down = dp[cur_row+1][cur_col]
                if obstacleGrid[cur_row][cur_col] == 0:
                    
                    if cur_row == row - 1 and cur_col == col - 1:
                        dp[cur_row][cur_col] = 1
                    else:
                        dp[cur_row][cur_col] = rt + down

                cur_row -=1
            cur_col -=1
        return dp[0][0]
