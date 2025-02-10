from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        self.ans = []
        self.visited = set()
        self.getKSum(nums,0,4,[],target)

        return self.ans

    def getKSum(self,nums,start,k,cur_quad,target):
        # print("nums len", len(nums))
        if not nums or len(nums) < k :
            return 
        

        if k > 2:
            for i in range(start,len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                self.getKSum(nums,i+1,k-1,cur_quad+[nums[i]],target-nums[i])

        else:
            lft = start
            rt = len(nums)-1
            while lft < rt:
                if nums[lft] + nums[rt] < target:
                    lft +=1
                elif nums[lft] + nums[rt] > target:
                    rt -=1
                else:
                    self.ans.append(cur_quad+[nums[lft],nums[rt]])
                    lft +=1
                    while lft < rt and nums[lft] == nums[lft-1]:
                        lft +=1