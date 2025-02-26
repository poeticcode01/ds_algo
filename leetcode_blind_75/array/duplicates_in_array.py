from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = [[num,False] for num in nums]

        duplicates = []
        for ind,itm in enumerate(nums):
            
            if nums[itm[0]-1][1]:
                duplicates.append(itm[0])
            else:
                nums[itm[0]-1][1] = True
        return duplicates