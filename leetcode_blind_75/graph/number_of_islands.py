from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_cnt = len(grid)
        col_cnt = len(grid[0])

        visited = set()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        island_count = 0

        for cur_row in range(row_cnt):
            for cur_col in range(col_cnt):
                if (cur_row,cur_col) in visited or grid[cur_row][cur_col] == "0":
                    continue
                visited.add((cur_row,cur_col))
                dq = deque([(cur_row,cur_col)])
                island_count +=1
                while dq:
                    k = dq.popleft()
                    for cur_dir in dirs:
                        new_row = k[0] + cur_dir[0]
                        new_col = k[1] + cur_dir[1]
                        if (0<=new_row<row_cnt) and (0<=new_col<col_cnt) and (new_row,new_col) not in visited and grid[new_row][new_col] == "1":
                            visited.add((new_row,new_col))
                            dq.append((new_row,new_col))

        return island_count