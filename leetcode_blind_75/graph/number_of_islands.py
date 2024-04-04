from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.row_cnt = len(grid)
        self.col_cnt = len(grid[0])
        self.grid = grid

        self.visit_set = set()
        ans = 0
        for row in range(self.row_cnt):
            for col in range(self.col_cnt):
                if (row,col)  in self.visit_set or grid[row][col] == "0":
                    continue
                ans +=1
                self.visit_set.add((row,col))
                self.dfs(row,col)

        return ans

    def dfs(self,row,col):
        if row < 0 or col < 0 or row >= self.row_cnt or col >= self.col_cnt:
            return

        neighbors = [(row,col-1),(row,col+1),(row-1,col),(row+1,col)]

        for frnd in neighbors:
            if frnd[0] < 0 or frnd[1] < 0 or frnd[0] >= self.row_cnt or frnd[1] >= self.col_cnt:
                continue
            if frnd in self.visit_set or self.grid[frnd[0]][frnd[1]] == "0":
                continue
            self.visit_set.add(frnd)
            self.dfs(frnd[0],frnd[1])

if __name__ == "__main__":
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    Solution().numIslands(grid)