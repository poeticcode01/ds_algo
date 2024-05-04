from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = None
        min_len = 0

        strt = 0
        end = 0
        run_sum = 0
        while strt <= end and end < len(nums):
            run_sum += nums[end]
            while run_sum >= target and strt <= end:
                if ans is None:
                    ans = min_len
                    min_len = end-strt+1
                else:
                    temp = end-strt+1
                    min_len = min(temp,min_len)
                run_sum -= nums[strt]
                strt +=1
            end +=1
        return min_len