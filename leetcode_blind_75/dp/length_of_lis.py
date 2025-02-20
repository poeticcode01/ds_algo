from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums)+1)
        dp[0] = 0
        ans = 1
        for i in range(2,len(nums)+1):
            for j in range(1,i):
                if nums[j-1] < nums[i-1]:
                    dp[i] = max(dp[i],dp[j]+1) 
                    ans = max(ans,dp[i])

        return ans

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         lis = [nums[0]]
#         for itm in nums[1:]:
#             if itm > lis[-1]:
#                 lis.append(itm)
#             elif itm < lis[-1]:
#                 ind = self.find_index(lis,itm)
#                 lis[ind] = itm
#         return len(lis)

#     def find_index(self,lis,key):
#         strt = 0
#         end = len(lis) - 1
#         while strt <= end:
#             mid = strt + (end-strt)//2
#             if lis[mid] < key:
#                 strt = mid + 1
#             else:
#                 end = mid - 1
#         return strt