class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        dp = [[False]*s_len for itm in range(s_len)]
        for i in range(s_len):
            dp[i][i] = True
        cur_len = 2
        ans = 1
        ans_str = s[0]
        while cur_len <= s_len:
            i = 0
            while i + cur_len - 1 < s_len:
                if cur_len == 2:
                    if s[i] == s[i+1]:
                        dp[i][i+1] = True
                        if ans < cur_len:
                            ans = cur_len
                            ans_str = s[i:i+cur_len]
                    else:
                        dp[i][i+1] = False

                else:
                    if s[i] == s[i+cur_len-1] and dp[i+1][i+cur_len-2]:
                        dp[i][i+cur_len-1] = True
                        if ans < cur_len:
                            ans = cur_len
                            ans_str = s[i:i+cur_len]
                    else:
                        dp[i][i+cur_len-1] = False
                i +=1
            cur_len +=1
        return ans_str
    
if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))