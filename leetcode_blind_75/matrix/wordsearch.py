from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visit_set = set()
        for cur_row,row_list in enumerate(board):
            for cur_col , col_itm in enumerate(row_list):
                visit_set.add((cur_row,cur_col))
                ans = self.dfs(cur_row,cur_col,col_itm,word,row,col,board,visit_set)
                visit_set.remove((cur_row,cur_col))
                if ans:
                    return True
        return False

    def dfs(self,cur_row,cur_col,run_str,word,row,col,board,visit_set):
        if run_str == word:
            return True

        for i in range(cur_row-1,cur_row+2):
            if i >= row or i < 0:
                continue 
            for j in range(cur_col-1,cur_col+2):
                if j >= col or j < 0:
                    continue
                if (i,j) in visit_set:
                    continue
                if ((i == cur_row -1) and ((j == cur_col - 1)or (j == cur_col + 1))) or ((i == cur_row + 1) and ((j == cur_col - 1)or (j == cur_col + 1))):
                    continue
                visit_set.add((i,j))
                temp_str = run_str + board[i][j]
                ans = self.dfs(i,j,temp_str,word,row,col,board,visit_set)
                if ans:
                    return True
                visit_set.remove((i,j))
        return False