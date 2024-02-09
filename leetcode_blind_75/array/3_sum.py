from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)-1):
            k = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp_sum = k + nums[l] + nums[r]
                if temp_sum == 0:
                    triplet = (k,nums[l],nums[r])
                    if triplet not in ans:
                        ans.add(triplet)
                    l +=1
                    r -=1
                elif temp_sum < 0:
                    l +=1
                else:
                    r -=1
        ans = [list(itm) for itm in ans]
        return ans
