import heapq
from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        i = 0
        freq_table = defaultdict(int)
        for itm in nums:
            freq_table[itm] +=1
        
        for key,val in freq_table.items():
            if i < k:
                heapq.heappush(min_heap,(val,key))
            else:
                if val > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(val,key))
            i +=1
        
        ans = []
        while min_heap:
            ans.append(heapq.heappop(min_heap)[1])
        return ans


        