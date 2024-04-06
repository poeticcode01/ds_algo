from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        begin = 0 
        end = 1
        ans = 1
    
        while begin < end and end < len(nums):
            if (nums[end] - nums[end-1]) != 0 and  (nums[end] - nums[end-1]) != 1 :
            
                begin = end
                end = end + 1 
                continue
            else:
                end +=1
                ans = max(ans,(end-begin))
        return ans