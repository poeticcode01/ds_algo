from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        

        total_sum = sum(nums)
        max_glob_sum = self.get_global_max(nums)
        if max_glob_sum < 0:
            return max_glob_sum

        min_glob_sum = self.get_global_min(nums)
        
        return max((total_sum - min_glob_sum),max_glob_sum)

    def get_global_min(self,nums):
        strt = 0
        end = 1

        n = len(nums)      
        cur_min_sum = nums[strt]
        min_glob_sum = nums[strt]

        while end < n:
            temp = cur_min_sum + nums[end]
            if temp <= nums[end]:
                cur_min_sum= temp
            else:
                strt = end
                cur_min_sum = nums[end]
            
            min_glob_sum = min(cur_min_sum ,min_glob_sum)

            end +=1
        return min_glob_sum

    def get_global_max(self,nums):
        strt = 0
        end = 1

        n = len(nums)

        
        cur_max_sum = nums[strt]
        max_glob_sum = nums[strt]

        while end < n:
            temp = cur_max_sum + nums[end]
            if temp >= nums[end]:
                cur_max_sum = temp
            else:
                strt = end
                cur_max_sum = nums[end]
            
            max_glob_sum = max(cur_max_sum ,max_glob_sum)

            end +=1
        return max_glob_sum
