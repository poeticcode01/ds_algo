from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        #1 Solution
        A = height
        rain_trap=0
        n=len(A)
        left_max_prefix=[0]*n
        left_max_prefix[0]=A[0]
        right_max_suffix=[0]*n
        right_max_suffix[-1]=A[n-1]
        for i in range(1,len(A)):
            if(A[i]>left_max_prefix[i-1]):
                left_max_prefix[i]=A[i]
            else:
                left_max_prefix[i]=left_max_prefix[i-1]
        for i in range(n-2,-1,-1):
            if(A[i]>right_max_suffix[i+1]):
                right_max_suffix[i]=A[i]
            else:
                right_max_suffix[i]=right_max_suffix[i+1]
        for i in range(n):
            rain_trap +=min(left_max_prefix[i],right_max_suffix[i])-A[i]
        return rain_trap


        #2 Solution

        # prev_ge = self.prev_greater(height)
        # next_ge = self.next_greater(height)
        # # print(prev_ge)
        # # print(next_ge)
        # i = 0
        # hlen = len(height)
        # ans = 0
        # seen = set()
        # while i < hlen:
            
        #     prev = height[prev_ge[i]]
        #     nxt = height[next_ge[i]]

        #     min_height = min(prev,nxt)
        #     temp = (min_height-height[i])*(next_ge[i]-prev_ge[i]-1) 
        #     if temp > 0 and (prev_ge[i],next_ge[i]) not in seen:
        #         # print(i,temp,prev_ge[i],next_ge[i])
        #         seen.add((prev_ge[i],next_ge[i]))
        #         ans += temp
        #     i +=1
        # return ans

        
    def next_greater(self,height):
        hlen = len(height)
        ans = [j for j in range(hlen)]
        stck = [0]
        i = 1
        while i < hlen:
            if height[i] <= height[stck[-1]]:
                stck.append(i)
            else:
                while stck and height[i] > height[stck[-1]]:
                    k = stck.pop()
                    ans[k] = i
                stck.append(i)
            i +=1
        return ans

    def prev_greater(self,height):
        hlen = len(height)
        ans = [j for j in range(hlen)]
        stck = [hlen-1]
        i = hlen-2
        while i >= 0:
            if height[i] <= height[stck[-1]]:
                stck.append(i)
            else:
                while stck and height[i] > height[stck[-1]]:
                    k = stck.pop()
                    ans[k] = i
                stck.append(i)
            i -=1
        return ans