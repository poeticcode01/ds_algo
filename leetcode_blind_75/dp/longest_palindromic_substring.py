class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[False]*s_len for i in range(s_len)]
        for i in range(s_len):
            dp[i][i] = True

        max_len = 1
        ans = s[0]
        for cur_len in range(s_len+1):
            if cur_len < 2:
                continue

            i = 0
            while i + cur_len - 1 < s_len:
                if cur_len == 2:
                    if s[i] == s[i+cur_len - 1]:
                        dp[i][i+cur_len - 1] = True
                else:
                    if s[i] == s[i+cur_len - 1]:
                        dp[i][i+cur_len - 1] = dp[i+1][i+cur_len - 2]

                if dp[i][i+cur_len - 1]:
                    if cur_len > max_len:
                        max_len = len(ans)
                        ans = s[i:i+cur_len]
                i +=1

        return ans