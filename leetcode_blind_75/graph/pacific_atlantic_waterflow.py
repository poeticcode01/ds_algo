from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.visit_set = set()
        self.is_pacific = dict()
        self.is_atlantic = dict()
        self.row_cnt = len(heights)
        self.col_cnt = len(heights[0])
        self.heights = heights
        self.ans = []

        for row in range(self.row_cnt):
            for col in range(self.col_cnt):
            
                self.visit_set.add((row,col))
                self.dfs(row,col)
                self.visit_set.remove((row,col))
                if self.is_pacific[(row,col)] and self.is_atlantic[(row,col)]:
                    self.ans.append([row,col])
        return self.ans
                

    def dfs(self,row,col):
        is_pacific = False
        is_atlantic = False

        if row < 0 or col < 0:
            is_pacific = True
        if row >= self.row_cnt or col >= self.col_cnt:
            is_atlantic = True

        if row < 0 or col < 0 or row >= self.row_cnt or col >= self.col_cnt:
            return is_pacific,is_atlantic
        
    

        neighbors = [(row,col-1),(row,col+1),(row+1,col),(row-1,col)]
        depth = self.heights[row][col]
        for frnd in neighbors:
            if frnd[0] < 0 or frnd[1] < 0 or frnd[0] >= self.row_cnt or frnd[1] >= self.col_cnt:
                if frnd[0] < 0 or frnd[1] < 0:
                    is_pacific = True
                if frnd[0] >= self.row_cnt or frnd[1] >= self.col_cnt:
                    is_atlantic = True

                if is_pacific and is_atlantic:
                    
                    self.is_pacific[(row,col)] = True
                    self.is_atlantic[(row,col)] = True
                    return True,True
                continue

            frnd_depth = self.heights[frnd[0]][frnd[1]]
            if frnd_depth > depth:
                continue

            if frnd in self.visit_set :
                continue

            
            self.visit_set.add(frnd)
            cur_pacific,cur_atlantic = self.dfs(frnd[0],frnd[1])
            self.visit_set.remove(frnd)
            if cur_pacific and cur_atlantic:
                
                self.is_pacific[(row,col)] = True
                self.is_atlantic[(row,col)] = True
                return True,True

            if cur_pacific:
                is_pacific = True
            if cur_atlantic:
                is_atlantic = True
            if is_pacific and is_atlantic:
                
                self.is_pacific[(row,col)] = True
                self.is_atlantic[(row,col)] = True
                return True,True
        if not self.is_pacific.get((row,col)):
            self.is_pacific[(row,col)] = is_pacific 
        if not self.is_atlantic.get((row,col)):
            self.is_atlantic[(row,col)] = is_atlantic

    
        return is_pacific,is_atlantic
    
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(heights))