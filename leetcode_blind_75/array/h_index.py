from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = len(citations)
        while ans >= 0:
            cnt = 0
            for ind,itm in enumerate(citations):
                if itm >= ans:
                    cnt +=1
            if cnt >= ans:
                return ans
            ans -=1
        return ans