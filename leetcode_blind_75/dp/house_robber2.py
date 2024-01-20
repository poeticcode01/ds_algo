from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums0 = nums[:-1]
        dp = [0 for i in range(len(nums0))]
        
        dp[0] = nums0[0]
    
        for i in range(1,len(nums0)):
            select = nums0[i]
            if i-2 >= 0:
                select = dp[i-2] + select
            unselect = dp[i-1]
            dp[i] = max(select,unselect)
            
        nums1 = nums[1:]
        dp1 = [0 for i in range(len(nums1))]
        dp1[0] = nums1[0]
        for i in range(1,len(nums1)):
            select = nums1[i]
            if i-2 >= 0:
                select = dp1[i-2] + select
            unselect = dp1[i-1]
            dp1[i] = max(select,unselect)
            
        ans = max(dp1[-1],dp[-1])
        # ans = max(max_money,ans)

        return ans
    
if __name__ == "__main__":
    nums = [1,2,1,1]
    print(Solution().rob(nums))