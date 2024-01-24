from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None]*(amount+1)
        return self.mincoin(amount,coins,dp)


    def mincoin(self,amount,coins,dp):
        if amount == 0:
            return 0
        if dp[amount] is not None:
            return dp[amount]
        min_denom = -1
        for coin in coins:
            if amount - coin < 0:
                continue
            temp = self.mincoin(amount-coin,coins,dp)
            if temp == -1:
                continue
            ans = 1 + temp
            if min_denom == -1:
                min_denom = ans
            else:
                min_denom = min(min_denom,ans)
        
        dp[amount] = min_denom
        return min_denom