from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)

        dp = [False for itm in range(s_len+1)]
        dp[0] = True
        word_set = set(wordDict)
        
        cur_len = 1
        while cur_len <= s_len:
            if cur_len - 20 < 0:
                strt = 0
            else:
                strt = cur_len - 20
            for slice in range(strt,cur_len):
                if dp[slice] and s[slice:cur_len] in word_set:
                    dp[cur_len] = True
                    break
            cur_len +=1
        return dp[s_len]