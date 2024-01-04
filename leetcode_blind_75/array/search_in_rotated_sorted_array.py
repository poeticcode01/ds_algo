from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1

        return self.bin_search(nums,low,high,target)

    def bin_search(self,nums,low,high,target):
        if low > high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid

        if nums[mid] > nums[low]:
            # if target < nums[mid]:
            ans = self.bin_search(nums,low,mid-1,target)
            if ans == -1:
                return self.bin_search(nums,mid+1,high,target)
        else:
            ans = self.bin_search(nums,mid+1,high,target)
            if ans == -1:
                return self.bin_search(nums,low,mid-1,target)

        return ans
    
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums,target))