from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0

        while i < j:
            temp = min(height[i],height[j])*(j-i)
            ans = max(ans,temp)
            if height[i] <= height[j]:
                i +=1
            else:
                j -=1
        return ans