from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def mark_unsurrounded_region(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != "O":
                return

            board[r][c] = "U"
            mark_unsurrounded_region(r+1,c)
            mark_unsurrounded_region(r-1,c)
            mark_unsurrounded_region(r,c-1)
            mark_unsurrounded_region(r,c+1)

        # Mark all Unsurrounded Region with "U"
        for cur_row in range(row):
            for cur_col in range(col):
                if cur_row in [0,row-1] or cur_col in [0,col-1]:
                    mark_unsurrounded_region(cur_row,cur_col)
        
        # Mark Surrounded region with "X"
        for cur_row in range(row):
            for cur_col in range(col):
                if board[cur_row][cur_col] == "O":
                    board[cur_row][cur_col] = "X"

        # Unmark Unsurrounded region back with "0"
        for cur_row in range(row):
            for cur_col in range(col):
                if board[cur_row][cur_col] == "U":
                    board[cur_row][cur_col] = "O"