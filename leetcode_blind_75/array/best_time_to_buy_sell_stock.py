from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = prices[0]
        for itm in prices[1:]:
            max_profit = max(max_profit,itm-min_so_far)
            min_so_far = min(min_so_far,itm)
        return max_profit