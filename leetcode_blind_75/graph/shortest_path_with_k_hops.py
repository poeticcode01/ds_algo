from collections import defaultdict
import heapq
from typing import List
class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        edge_graph = defaultdict(list)
        for end1, end2,wt in edges:
            edge_graph[end1].append((end2,wt))
            edge_graph[end2].append((end1,wt))

        min_heap = [(0,s,0)]
        visited = [[float('inf')]*(k+2) for _ in range(n)]
        visited[s][0] = 0

        while min_heap:
            cost,city,stops = heapq.heappop(min_heap)
            # print(cost,city,stops)
            if city == d:
                return cost
            if cost > visited[city][stops]:
                continue
            

            for frnd , wt in edge_graph[city]:
                new_wt1 = wt + cost
                new_wt2 = cost
                # without hop
                if new_wt1 < visited[frnd][stops]:
                    visited[frnd][stops] = new_wt1
                    heapq.heappush(min_heap,(new_wt1,frnd,stops))
                # with hop
                if stops < k and new_wt2 < visited[frnd][stops+1]:
                    visited[frnd][stops+1] = new_wt2
                    heapq.heappush(min_heap,(new_wt2,frnd,stops+1))