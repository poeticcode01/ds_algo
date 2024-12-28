from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        strt = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        end = 1
        cur_max_sum = nums[strt]
        max_glob_sum = nums[strt]

        cur_min_sum = nums[strt]
        min_glob_sum = nums[strt]

        total_sum = sum(nums)

        while end < n:
            temp = cur_max_sum + nums[end]
            if temp >= nums[end]:
                cur_max_sum = temp
            else:
                strt = end
                cur_max_sum = nums[end]
            
            max_glob_sum = max(cur_max_sum ,max_glob_sum)

            end +=1
        end = 1
        while end < n:
            temp = cur_min_sum + nums[end]
            if temp <= nums[end]:
                cur_min_sum= temp
            else:
                strt = end
                cur_min_sum = nums[end]
            
            min_glob_sum = min(cur_min_sum ,min_glob_sum)

            end +=1

        if max_glob_sum < 0:
            return max_glob_sum
        # print(total_sum,min_glob_sum,max_glob_sum)
        return max((total_sum - min_glob_sum),max_glob_sum)