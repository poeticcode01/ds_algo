import sys
from typing import List
sys.setrecursionlimit(1000006)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first_ind = self.firstElement(low,high,nums,target)
        last_ind = self.lastElement(low,high,nums,target)
        return [first_ind,last_ind]

    def firstElement(self,low,high,nums,target):
        
        if low > high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            if low == high or (high-low) == 1:
                return low
            
            else:
                return self.firstElement(low,mid,nums,target)
        elif nums[mid] > target:
            return self.firstElement(low,mid-1,nums,target)
        else:
            return self.firstElement(mid+1,high,nums,target)

    def lastElement(self,low,high,nums,target):
        
        if low > high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            if low == high:
                return low
            elif high-low == 1:
                if nums[high] == target:
                    return high
                else:
                    return low
            else:
                return self.lastElement(mid,high,nums,target)
        elif nums[mid] > target:
            return self.lastElement(low,mid-1,nums,target)
        else:
            return self.lastElement(mid+1,high,nums,target)