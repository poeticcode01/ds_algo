import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        current_capital = w
        project_index = 0
        
        for _ in range(k):
            # Push all projects that can be started with the current capital into the max heap
            while project_index < n and projects[project_index][0] <= current_capital:
                # Use a negative profit to simulate max heap with heapq (which is a min heap by default)
                heapq.heappush(max_heap, -projects[project_index][1])
                project_index += 1

            # If no projects can be started with the current capital, stop
            if not max_heap:
                break
            
            # Pop the most profitable project (invert the sign back)
            current_capital += -heapq.heappop(max_heap)
        
        return current_capital