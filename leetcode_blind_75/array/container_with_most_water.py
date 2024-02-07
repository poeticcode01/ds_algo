from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        A= height
        if len(A) == 1:
            return 0
        i = 0
        j = len(A) - 1
        ans = -1
        while i < j:
            k = min(A[i],A[j])
            ans = max(ans,(j-i)*k)
            if A[i] < A[j]:
                i +=1
            else:
                j -=1
        return ans