from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        run_ptr = 0
        while run_ptr < len(nums):
            while run_ptr < len(nums) and nums[run_ptr] == nums[i]:
                run_ptr +=1
            if run_ptr < len(nums):
                nums[i+1],nums[run_ptr] = nums[run_ptr],nums[i+1]
            else:
                return i + 1
            run_ptr +=1
            i +=1
        return i + 1