from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_len = len(prices)
        if price_len == 1:
            return 0
        profit = 0
        for i in range(1,price_len):
            if prices[i] > prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit

        # dp = [0 for i in range(price_len)]
        # # dp[0] = 0
        # if prices[1] >= prices[0]:
        #     dp[1] = prices[1] - prices[0]
        # # else:
        # #     dp[1] = 0

        # ans = dp[1]
        
        # for i in range(2,price_len):
        #     dp[i] = dp[i-1]
        #     for j in range(i):
        #         if prices[i] >= prices[j]:
        #             temp = dp[j] +  (prices[i] - prices[j])
        #             dp[i] = max(dp[i],temp)
        #     # ans = max(ans,dp[i])
        # return max(dp)
        