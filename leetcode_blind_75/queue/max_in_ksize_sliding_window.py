from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #1. move to new element in nums  , compare with previous in queue
            #2.a if lesser, insert
            #2.b else , remove elements which all are lesser than that
        #3. at each window , get bottom most element as ans to that window

        ans = []
        i = 0
        dq = deque([])
        while i < len(nums):
            if not dq:
                dq.append(i)

            #removing out of window element
            while dq and i-dq[0] >= k:
                dq.popleft()

            #removing irrelevant elements 
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop() 

            dq.append(i)
            if i < k-1:
                i +=1
                continue


            ans.append(nums[dq[0]])
            i +=1
        return ans

        