from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        strt = 0
        end = 0
        ans = []
        i = 1
        
        while i < len(nums):
            if not (nums[i] >= nums[i-1] and nums[i]-nums[i-1] <= 1):
                if end > strt:
                    ans.append(f"{nums[strt]}->{nums[end]}")
                else:
                    ans.append(f"{nums[strt]}")
                strt = i
                end = i
            else:
                end = i
            i +=1
            
        
        if end > strt:
            ans.append(f"{nums[strt]}->{nums[end]}")
        else:
            ans.append(f"{nums[strt]}")

        return ans