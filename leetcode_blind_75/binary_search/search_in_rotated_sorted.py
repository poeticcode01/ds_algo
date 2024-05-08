from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        flag,ans = self.bin_search(low,high,target,nums)
        return ans

    def bin_search(self,low,high,target,nums):
        if low > high:
            return False,-1
        mid = low + (high-low)//2
        if target ==  nums[mid]:
            return True,mid
        
        # if nums[mid] >= nums[low] and nums[mid] <= nums[high]:
        #     if 
        #     return self.bin_search(low,mid-1,target)
        # else:
        flag,ans = self.bin_search(low,mid-1,target,nums)
        if flag:
            return flag,ans
        else:
            return self.bin_search(mid+1,high,target,nums)