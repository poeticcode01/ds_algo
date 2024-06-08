from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if len(nums) <= 1:
        #     return 0 if val in nums else 1

        i = 0
        j = len(nums) - 1
        # flag = False
        while i <= j:
            if nums[i] != val:
                i +=1
                # flag = True
                continue
            
            nums[i],nums[j] = nums[j],nums[i]
            j -=1

        return i 