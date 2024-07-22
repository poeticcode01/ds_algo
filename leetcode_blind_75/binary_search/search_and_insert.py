from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return high + 1

        return self.bin_search(low,high,target,nums)

    def bin_search(self,low,high,target,nums):
        if low > high:
            return low
        if low == high:
            # return low
            if nums[low] >= target:
                return low
            else:
                return low + 1
            # else:
            #     return low - 1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bin_search(mid+1,high,target,nums)
        else:
            return self.bin_search(low,mid -1,target,nums)
        

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 2

    Solution().searchInsert(nums,target)