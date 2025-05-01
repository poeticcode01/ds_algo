import heapq
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        min_heap = [(0,0,0)]

        row = len(moveTime)
        col = len(moveTime[0])
        visited = set()
        visited.add((0,0))
        # print(min_heap)
        while min_heap:
            # print("here")
            # print(min_heap)
            cost,cur_row,cur_col = heapq.heappop(min_heap)
            if cur_row == row - 1 and cur_col == col - 1:
                return cost
            for i in range(cur_row-1,cur_row+2):
                if i < 0 or i >= row:
                    continue
                j = cur_col
                if (i,j) not in visited:
                    visited.add((i,j))
                    new_time = max(cost,moveTime[i][j]) + 1
                    heapq.heappush(min_heap,(new_time,i,j))

            for j in range(cur_col-1,cur_col+2):
                if j < 0 or j >= col:
                    continue
                i = cur_row
                if (i,j) not in visited:
                    visited.add((i,j))
                    new_time = max(cost,moveTime[i][j]) + 1
                    heapq.heappush(min_heap,(new_time,i,j))