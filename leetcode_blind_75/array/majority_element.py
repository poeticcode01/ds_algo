from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 1
        maj_ind = 0
        cnt = 1
        while i < len(nums):
            if nums[maj_ind] != nums[i]:
                cnt -=1
            else:
                cnt +=1
            if cnt == 0:
                cnt = 1
                maj_ind = i
            i +=1
        return nums[maj_ind]
        