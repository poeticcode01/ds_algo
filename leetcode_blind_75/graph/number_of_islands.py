from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        visited = set()
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans +=1
                    # print(visited,(i,j))
                    visited.add((i,j))
                    dq = deque([(i,j)])
                    while dq:
                        cur_row,cur_col = dq.popleft()
                        # print(cur_row,cur_col)
                        neighbors = [(cur_row-1,cur_col),(cur_row+1,cur_col),
                                    (cur_row,cur_col-1),(cur_row,cur_col+1)]
                        # print(neighbors)
                        for frnd in neighbors:
                            # print(frnd,(i,j))
                            
                            if frnd[0] >= row or frnd[0] < 0 or frnd[1] >= col or frnd[1] < 0:
                                # print("neighbor_friends",frnd,(i,j))
                                continue
                            # print("neighbor_friends",frnd,(i,j))
                            if grid[frnd[0]][frnd[1]] == "1" and frnd not in visited:
                                # print("here")
                                visited.add(frnd)
                                dq.append(frnd)



                else:
                    continue
        return ans

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    Solution().numIslands(grid)