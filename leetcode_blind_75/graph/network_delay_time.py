import heapq
from collections import defaultdict
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_graph = defaultdict(list)
        for src, dest, tim in times:
            edge_graph[src].append((dest,tim))

        visited = set()
        min_heap = [(0,k)]
        min_time = 0
        while min_heap:
            tm, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            min_time = max(min_time,tm)

            for frnd,frnd_time in edge_graph[node]:
                # if frnd not in visited:
                heapq.heappush(min_heap,(tm+frnd_time,frnd))

        if len(visited) == n:
            return min_time
        return -1