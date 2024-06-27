from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1 to 0 --> 10
        # 0 to 1 --> 100
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        for i in range(self.row):
            for j in range(self.col):
                cur_val = board[i][j]
                zero_cnt, one_cnt = self.get_neighbor_count(i,j)
                # print(i,j,zero_cnt,one_cnt,cur_val)
                if cur_val == 1:
                    if one_cnt < 2 or one_cnt > 3:
                        board[i][j] = 10
                else:
                    if one_cnt == 3:
                        # print(i,j)
                        board[i][j] = 100

        # print(board)
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == 10:
                    board[i][j] = 0
                if board[i][j] == 100:
                    board[i][j] = 1



    def get_neighbor_count(self,cur_row,cur_col):
        zero_cnt = 0
        one_cnt = 0
        for i in range(cur_row-1,cur_row+2):
            if i < 0 or i >= self.row:
                continue
            for j in range(cur_col-1,cur_col+2):
                if j < 0 or j >= self.col:
                    continue
                if i == cur_row and j == cur_col:
                    continue
                if self.board[i][j] == 0 or self.board[i][j] == 100:
                    zero_cnt +=1
                if self.board[i][j] == 1 or self.board[i][j] == 10:
                    one_cnt +=1

        return zero_cnt,one_cnt