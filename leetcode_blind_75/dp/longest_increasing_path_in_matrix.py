from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.row_cnt = len(matrix)
        self.col_cnt = len(matrix[0])
        if self.row_cnt == 1 and self.col_cnt == 1:
            return 1
        self.matrix = matrix
        self.dp = [[1]*self.col_cnt for i in range(self.row_cnt)]
        visited = set()
        self.dir = [[-1,0],[1,0],[0,-1],[0,1]]
        self.max_len = 1 
        for cur_row in range(self.row_cnt):
            for cur_col  in range(self.col_cnt):
                
                for row_incr,col_incr in self.dir:
                    new_row = cur_row+row_incr
                    new_col = cur_col+col_incr
                    if (0<=new_row<self.row_cnt) and (0<=new_col<self.col_cnt)  and (matrix[new_row][new_col] > matrix[cur_row][cur_col]):
                      if (new_row,new_col) in visited:
                        self.dp[cur_row][cur_col] = max(self.dp[cur_row][cur_col],self.dp[new_row][new_col]+1)
                      else:
                        self.dfs(new_row,new_col,visited)
                        self.dp[cur_row][cur_col] = max(self.dp[cur_row][cur_col],self.dp[new_row][new_col]+1)
     
                self.max_len = max(self.max_len,self.dp[cur_row][cur_col])
                visited.add((cur_row,cur_col))
                      
        
        return self.max_len

    def dfs(self,cur_row,cur_col,visited):
        for row_incr,col_incr in self.dir:
            new_row = cur_row+row_incr
            new_col = cur_col+col_incr
            if (0<=new_row<self.row_cnt) and (0<=new_col<self.col_cnt) and (self.matrix[new_row][new_col] > self.matrix[cur_row][cur_col]):
                if (new_row,new_col) in visited:
                    self.dp[cur_row][cur_col] = max(self.dp[cur_row][cur_col],self.dp[new_row][new_col]+1)
                else:
                    self.dfs(new_row,new_col,visited)
                    self.dp[cur_row][cur_col] = max(self.dp[cur_row][cur_col],self.dp[new_row][new_col]+1)

            

        self.max_len = max(self.max_len,self.dp[cur_row][cur_col])     
        visited.add((cur_row,cur_col))