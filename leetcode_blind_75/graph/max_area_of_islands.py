from collections import deque
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        max_area = 0
        visited = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for cur_row in range(row_len):
            for cur_col in range(col_len):
                if (cur_row,cur_col) in visited or grid[cur_row][cur_col] == 0:
                    continue
                visited.add((cur_row,cur_col))
                dq = deque([(cur_row,cur_col)])
                count = 0
                while dq:
                    k = dq.popleft()
                    count +=1
                    for new_dir in dirs:
                        new_row = k[0]+new_dir[0]
                        new_col = k[1]+new_dir[1]
                        if (0<=new_row<row_len) and (0<=new_col<col_len) and (new_row,new_col) not in visited and grid[new_row][new_col] == 1:
                            visited.add((new_row,new_col))
                            dq.append((new_row,new_col))
                max_area = max(max_area,count)
        return max_area