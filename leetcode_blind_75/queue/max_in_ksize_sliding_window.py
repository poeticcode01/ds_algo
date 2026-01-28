from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #1. get next max element
        #2. insert an element , compare with previous
            #2.a if lesser, insert
            #2.b else , remove elements which all are lesser than that
        #3. at each window , get bottom most element as ans to that window

        ans = []
        i = 0
        dq = deque([])
        nge = self.next_ge(nums)
        while i < len(nums):
            if not dq:
                dq.append(i)

            #removing out of window element
            while dq and i-dq[0] >= k:
                dq.popleft()

            #removing irrelevant elements 
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop() 

            dq.append(i)
            if i < k-1:
                i +=1
                continue

            #for current window , find max in that window
            while len(dq) > 1:
                km = nge[dq[0]]
                if  km == -1 or  km > i:
                    break
                else:
                    while dq:
                        temp = dq[0]
                        if temp == km:
                            break
                        else:
                            dq.popleft()

            ans.append(nums[dq[0]])
            i +=1
        return ans



    def next_ge(self,nums):
        stck = [0]
        next_ge = [-1 for itm in nums]
        i = 1
        while i < len(nums):
            while stck and  nums[i] > nums[stck[-1]]:
                k = stck.pop()
                next_ge[k] = i
            stck.append(i)
            i +=1
        return next_ge

        