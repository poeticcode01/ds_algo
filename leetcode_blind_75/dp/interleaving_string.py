class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)

        if s1_len + s2_len != s3_len:
            return False

        dp = [[False]*(s2_len+1) for i in range(s1_len+1)]
        dp[0][0] = True
        
        for i in range(s1_len+1):
            for j in range(s2_len+1):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] and (s3[j-1] == s2[j-1])
                    continue
                if j == 0:
                    dp[i][j] = dp[i-1][j] and (s3[i-1] == s1[i-1])
                    continue

                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]

                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]

        return dp[s1_len][s2_len]