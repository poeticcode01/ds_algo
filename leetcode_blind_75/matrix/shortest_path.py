class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        obstacle_list = []

        row_cnt = len(grid)
        col_cnt = len(grid[0])

        for cur_row   in range(row_cnt):
            for cur_col in range(col_cnt):
                if grid[cur_row][cur_col] == 1:
                    obstacle_list.append((cur_row,cur_col))

        dp = [float('inf')*col_cnt for i in range(row_cnt)]
        ans = float('inf')
        for cur_k in range(k):
            ans_set = [] 
            self.getAllKlenObstacles(obstacle_list,0,set(),cur_k,ans_set)
            for cur_set in ans_set:
                
                if grid[row_cnt-1][col_cnt-1] == 0:
                    dp[row_cnt-1][col_cnt-1] = 0
                else:
                    if (row_cnt-1,col_cnt-1) in cur_set:
                        dp[row_cnt-1][col_cnt-1] = 0
                col = cur_col - 1
                i = row -2
                while i >= 0:
                    if grid[i][col] == 1:
                        if (i,col) in cur_set:
                            dp[i][col] = 1 + dp[i+1][col]
                    else:
                        dp[i][col] = 1 + dp[i+1][col]
                    i -=1
                


                
                    






        
    def reset_dp(self):
        pass

    def getAllKlenObstacles(self,obstacles,offset,run_set,k,ans_set):
        if len(run_set) == k:
            ans_set.append(run_set)
            return

        temp = offset
        while temp < len(obstacles):
            new_set = run_set.union({obstacles[temp]})
            if len(new_set) <= k:
                self.getAllKlenObstacles(obstacles,temp+1,new_set,k,ans_set)
            self.getAllKlenObstacles(obstacles,temp+1,run_set,k,ans_set)
            temp +=1