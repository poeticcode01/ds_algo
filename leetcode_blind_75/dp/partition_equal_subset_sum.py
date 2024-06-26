from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        check_sum = total_sum//2
        return self.subset_sum(nums,check_sum)

    def subset_sum(self,nums,check_sum):
        dp = [[False]*(len(nums)+1) for i in range(check_sum+1)]
        dp[0][0] = True

        for cur_sum in range(check_sum+1):
            for j in range(1,len(nums)+1):
                
                if dp[cur_sum][j-1]:
                    dp[cur_sum][j] = True
                else:
                    rem = cur_sum - nums[j-1]
                    if rem < 0:
                        continue

                    dp[cur_sum][j] = dp[rem][j-1]
        return dp[check_sum][len(nums)]