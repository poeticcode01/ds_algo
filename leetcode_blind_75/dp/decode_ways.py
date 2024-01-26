class Solution:
    def numDecodings(self, s: str) -> int:
        s_len = len(s)
        dp = [0 for i in range(s_len+1)]
        dp[0] = 1
        if int(s[0]) != 0:
            dp[1] = 1
        for i in range(2,s_len+1):
            if int(s[i-2]) != 0: 
                temp = int(s[i-2:i])
                ans = 0
                if temp <= 26:
                    ans += dp[i-2]
                if int(s[i-1]) != 0:
                    ans += dp[i-1]
                dp[i] = ans
            else:
                if int(s[i-1]) != 0:
                    dp[i] = dp[i-1]
                
        return dp[s_len]