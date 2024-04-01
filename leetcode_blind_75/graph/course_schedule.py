from collections import defaultdict
import heapq
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = defaultdict(int)
        edge_map = defaultdict(list)
        min_heap = []
        for cur_course in prerequisites:
            indegree[cur_course[1]] +=1
            edge_map[cur_course[0]].append(cur_course[1])

        for course in range(numCourses):
            if indegree[course] == 0:
                heapq.heappush(min_heap,course)
        ans = 0
        while min_heap:
            k = heapq.heappop(min_heap)
            ans +=1
            for frnd in edge_map[k]:
                indegree[frnd] -=1
                if indegree[frnd] == 0:
                    heapq.heappush(min_heap,frnd)

        return ans == numCourses