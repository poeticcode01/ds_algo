import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap,nums[i])

        for i in range(k,nums_len):
            top_element = min_heap[0]
            if nums[i] > top_element:
                pop_element = heapq.heappop(min_heap)
                heapq.heappush(min_heap,nums[i])
                
        return min_heap[0]