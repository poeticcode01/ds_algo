from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        self.row_cnt = len(board[0])
        self.col_cnt = len(board[1])

        self.row_map = defaultdict(set)
        self.col_map = defaultdict(set)
        self.sub_box_map = defaultdict(set)

        self.is_valid = True
        self.build_map(board)

        return self.is_valid





    def build_map(self,board):

        for cur_row in range(self.row_cnt):

            for cur_col in range(self.col_cnt):

                val = board[cur_row][cur_col]
                if val == ".":
                    continue

                

                if val in self.row_map[cur_row]:
                    self.is_valid = False
                    # print(val)
                    # print("in row map",self.row_map,val,cur_row,cur_col)
                    return

                self.row_map[cur_row].add(val)

                if val in self.col_map[cur_col]:
                    self.is_valid = False
                    # print("in col map",self.col_map,val,cur_row,cur_col)
                    return

                self.col_map[cur_col].add(val)

                sub_box_pos = self.get_sub_box_pos(cur_row,cur_col)
                if val in self.sub_box_map[sub_box_pos]:
                    self.is_valid = False
                    # print("in sub box map",self.sub_box_map,val,cur_row,cur_col)
                    return

                self.sub_box_map[sub_box_pos].add(val)





    def get_sub_box_pos(self,cur_row,cur_col):

        if cur_row//3 == 0:
            sub_box_pos = cur_col//3
        elif cur_row//3 == 1:
            sub_box_pos = 3 + cur_col//3
        else:
            sub_box_pos = 6 + cur_col//3

        return sub_box_pos
            