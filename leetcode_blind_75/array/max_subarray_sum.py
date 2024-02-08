class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum = nums[0]
        ans = run_sum
        rt = 1
        while rt < len(nums):
            temp_sum = run_sum + nums[rt]
            if temp_sum < nums[rt]:
                run_sum = nums[rt]
            else:
                run_sum = temp_sum
            ans = max(run_sum,ans)
            rt +=1
        return ans