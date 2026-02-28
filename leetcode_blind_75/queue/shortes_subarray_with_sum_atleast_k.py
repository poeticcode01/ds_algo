from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        pref_sum = [0]
        dq = deque([])

        for ind,itm in enumerate(nums):
            pref_sum.append(pref_sum[-1]+itm)

        # print(pref_sum)
        ans = float('inf')
        for ind ,itm  in enumerate(pref_sum):

            while dq and pref_sum[ind] - pref_sum[dq[0]] >= k:
                lft_ind = dq.popleft()
                ans = min(ans,ind-lft_ind)

            while dq and pref_sum[ind] <= pref_sum[dq[-1]]:
                dq.pop()
            dq.append(ind)
            
            
                    
        return ans if ans != float("inf") else -1