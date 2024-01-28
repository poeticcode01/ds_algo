from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        nums_len = len(nums)
        i = 1
        while max_jump < (nums_len-1) and i < nums_len:
            if max_jump < i:
                return False
            temp_jump = i + nums[i]
            max_jump = max(max_jump,temp_jump)
            i +=1
        return True