from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_transaction_count = k
        days_len = len(prices)
        dp = [[0]*days_len for i in range(max_transaction_count+1)]
        

        for transaction_so_far in range(1,max_transaction_count+1):
            for days_so_far in range(1,days_len):
                dp[transaction_so_far][days_so_far ] = max(dp[transaction_so_far][days_so_far-1],self.sell_stock(transaction_so_far,days_so_far,dp,prices))

        return dp[k][days_len-1]

    def sell_stock(self,transaction_so_far,days_so_far ,dp,prices):
        max_profit = 0
        for day in range(days_so_far):
            sold_price = prices[days_so_far] - prices[day]
            if sold_price > 0:
                max_profit = max(max_profit,dp[transaction_so_far-1][day]+sold_price)
        return max_profit