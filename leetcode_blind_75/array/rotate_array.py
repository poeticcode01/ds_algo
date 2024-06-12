from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k%len(nums)
        part1 = nums[len(nums)-k:]
        part2 = nums[:len(nums)-k]

        i = 0
        for itm in part1:
            nums[i] = itm
            i +=1
        for itm in part2:
            nums[i] = itm
            i +=1
