from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high-low)//2
            if mid-1 >= 0:
                prev = nums[mid-1]
            else:
                prev = nums[mid] - 1

            if mid + 1 <= high:
                nxt = nums[mid + 1]
            else:
                nxt = nums[mid] - 1

            if nums[mid] > prev and nums[mid] > nxt:
                return mid
            elif nums[mid] < prev:
                high = mid -1
            else:
                low = mid + 1