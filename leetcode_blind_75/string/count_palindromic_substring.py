class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        ans = len(s)
        cur_len = 2
        while cur_len <= len(s):
            i = 0
            while i + cur_len - 1 < len(s):
                if cur_len == 2:
                    if s[i] == s[i+cur_len-1]:
                        dp[i][i+cur_len-1] = True
                        ans +=1
                else:
                    if s[i] == s[i+cur_len-1] and dp[i+1][i+cur_len-2]:
                        dp[i][i+cur_len-1] = True
                        ans +=1
                i +=1
            cur_len +=1
        return ans