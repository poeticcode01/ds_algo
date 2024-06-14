from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [i for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]+j >= i:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]