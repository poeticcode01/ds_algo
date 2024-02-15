from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(1,n+1):
            xor ^= i
        for i in range(n):
            xor ^=nums[i]
        return xor