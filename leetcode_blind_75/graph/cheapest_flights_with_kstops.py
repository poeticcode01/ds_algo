from collections import defaultdict,deque
from typing import List
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # PriorityQueue: (cost_so_far, current_city, stops_used)
        heap = [(0, src, 0)]

        # Tracks the minimal cost to reach a node with a certain number of stops
        visited = [[float('inf')] * (k + 2) for _ in range(n)]
        visited[src][0] = 0

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            for nei, price in graph[city]:
                next_cost = cost + price
                # Only consider this path if it's cheaper than previously recorded one at this stop level
                if next_cost < visited[nei][stops + 1]:
                    visited[nei][stops + 1] = next_cost
                    heapq.heappush(heap, (next_cost, nei, stops + 1))

        return -1