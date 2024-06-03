from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        row_len = len(matrix)
        col_len = len(matrix[0])

        dp = []
        for i in range(row_len):
            temp = []
            for j in range(col_len):
                temp.append(int(matrix[i][j]))
            dp.append(temp)
        # print(dp)
        ans = 0
        for i in range(row_len):
            for j in range(col_len):
                if dp[i][j] == 1:
                    up = 0
                    down = 0
                    diag = 0
                    if i-1 >= 0:
                        up = dp[i-1][j]
                    if j - 1 >= 0:
                        down = dp[i][j-1]
                    if i-1 >= 0 and j - 1 >= 0:
                        diag = dp[i-1][j-1]
                    dp[i][j] = min(min(up,down),diag)+1
                    # print(dp[i][j])
                    ans = max(ans,dp[i][j]**2)
        return ans