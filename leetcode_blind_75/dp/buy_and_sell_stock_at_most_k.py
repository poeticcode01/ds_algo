from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        days_len = len(prices)
        dp = [[0]*days_len for i in range(k+1)]

        for i in range(1,k+1):
            for j in range(1,days_len):
                dp[i][j] = max(dp[i][j-1],self.sell_stock(i,j,dp,prices))

        return dp[k][days_len-1]

    def sell_stock(self,i,j,dp,prices):
        max_profit = 0
        for day in range(j):
            sold_price = prices[j] - prices[day]
            if sold_price > 0:
                max_profit = max(max_profit,dp[i-1][day]+sold_price)
        return max_profit