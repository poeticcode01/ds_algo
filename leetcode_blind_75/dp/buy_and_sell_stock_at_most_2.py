from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_so_far = prices[0]
        price_len = len(prices)
        pref_dp = [0 for i in range(price_len)]
        pref_max = [0 for i in range(price_len)]
        max_profit = 0
        for i in range(1,price_len):
            if prices[i] >= min_so_far:
                pref_dp[i] = prices[i] - min_so_far
            
            min_so_far = min(min_so_far,prices[i])
            max_profit = max(max_profit,pref_dp[i])
            pref_max[i]= max(pref_max[i-1],pref_dp[i])

        max_so_far = prices[-1]
        suff_dp = [0 for i in range(price_len)]
        suff_max = [0 for i in range(price_len)]

        i = price_len - 2
        while i >= 0:
            if prices[i] <= max_so_far:
                suff_dp[i] = max_so_far - prices[i]

            max_profit = max(max_profit,suff_dp[i])
            max_so_far = max(max_so_far,prices[i])
            suff_max[i]= max(suff_max[i+1],suff_dp[i])
            i -=1

        for i in range(1,price_len-1):
            # pref_max = max(pref_dp[:i+1])
            # suff_max = max(suff_dp[i+1:])

            max_profit = max(max_profit,pref_max[i]+suff_max[i+1])
        # print(pref_dp,suff_dp)
        return max_profit