from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visit_set = set()
        for cur_row in range(row):
            for cur_col in range(col):
                col_itm = board[cur_row][cur_col]
                if col_itm != word[0]:
                    continue
                board[cur_row][cur_col] = "#"
                # visit_set.add((cur_row,cur_col))
                ans = self.dfs(cur_row,cur_col,0,word,row,col,board)
                # visit_set.remove((cur_row,cur_col))
                board[cur_row][cur_col] = col_itm
                if ans:
                    return True
        return False

    def dfs(self,cur_row,cur_col,ind,word,row,col,board):
        # if board[cur_row][cur_col] != word[ind]:
        #     return False
        if ind == len(word) - 1:
            return True

        neighbors_list = [(cur_row,cur_col-1),(cur_row,cur_col+1),(cur_row+1,cur_col),(cur_row-1,cur_col)]
        for neighbrs in neighbors_list:
            
            if neighbrs[0] < 0 or neighbrs[0] >= row or neighbrs[1] < 0 or neighbrs[1] >= col:
                continue
            if board[neighbrs[0]][neighbrs[1]] == "#":
                continue
            placeholder = board[neighbrs[0]][neighbrs[1]]
            if word[ind+1] != placeholder:
                continue
            board[neighbrs[0]][neighbrs[1]] = "#"
            
            ans = self.dfs(neighbrs[0],neighbrs[1],ind+1,word,row,col,board)
            if ans:
                return True
            board[neighbrs[0]][neighbrs[1]] = placeholder
        return False
