from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_cnt = len(grid)
        col_cnt = len(grid[0])
        if grid[0][0] or grid[row_cnt-1][col_cnt-1]:
            return -1

        dir = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        dq = deque([(0,0,1)])
        visited = set((0,0))
        while dq:
            row,col,steps = dq.popleft()
            if (row,col) == (row_cnt-1,col_cnt-1):
                return steps
            for row_inc,col_inc in dir:
                new_row = row+row_inc
                new_col = col+col_inc
                if (0<=new_row<row_cnt) and (0<=new_col<col_cnt) and (new_row,new_col) not in visited and not grid[new_row][new_col]:
                    visited.add((new_row,new_col))
                    dq.append((new_row,new_col,steps+1))
        return -1