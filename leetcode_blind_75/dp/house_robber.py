from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            select = nums[i]
            if i-2 >= 0:
                select = dp[i-2] + select
            unselect = dp[i-1]
            dp[i] = max(select,unselect)
        return dp[-1]