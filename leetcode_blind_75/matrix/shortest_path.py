from collections import deque
from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        

        row_cnt = len(grid)
        col_cnt = len(grid[0])

        if k >= (row_cnt-1) + (col_cnt-1):
            return row_cnt+col_cnt-2

        dq = deque([(0,(0,0,k))])
        visited = set((0,0,k))
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while dq:
            steps_taken,(cur_row,cur_col,remaining_eliminate) = dq.popleft()
            if cur_row == row_cnt-1 and cur_col == col_cnt-1:
                return steps_taken
            
            for row_increment , col_increment in directions:
                new_row = cur_row+row_increment
                new_col = cur_col+col_increment
                if (new_row >= 0 and new_row < row_cnt) and (new_col >= 0 and new_col < col_cnt):
                    new_remaining = remaining_eliminate - grid[new_row][new_col]
                    if new_remaining >= 0 and (new_row,new_col,new_remaining) not in visited:
                        visited.add((new_row,new_col,new_remaining))
                        dq.append((steps_taken+1,(new_row,new_col,new_remaining)))
        return -1