from collections import deque
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        strt = 1
        self.board = board

        self.row_cnt = len(board)
        self.col_cnt = len(board[0])


        self.board_size = self.row_cnt*self.col_cnt
        return self.get_min_steps()



    def get_min_steps(self):
        visited = set()
        dq = deque([(1,0)])
        visited.add(1)
        while dq:
            cur_pos,move_count = dq.popleft()
            if cur_pos == self.board_size:
                return move_count
            

            for indx in range(1,7):
                nxt_pos = cur_pos+indx

                if nxt_pos > self.board_size:
                    break

                row,col = self.get_cell_position(nxt_pos)
                if self.board[row][col] != -1:
                    nxt_pos = self.board[row][col]
                if nxt_pos not in visited:
                    visited.add(nxt_pos)
                    dq.append((nxt_pos,move_count+1))
        return -1

        



                



    def get_cell_position(self,position):
        col = position%self.row_cnt
        if col == 0:
            row = self.row_cnt - position//self.row_cnt
        else:
            row = self.row_cnt - position//self.row_cnt - 1

        if (self.row_cnt - 1 - row)%2:
            if col != 0:
                col = self.col_cnt-col
        else:
            if col != 0:
                col = col - 1
            else:
                col = self.col_cnt - 1

        return (row,col)

        
    
if __name__ == "__main__":
    board = [[-1,-1,27,13,-1,25,-1],
             [-1,-1,-1,-1,-1,-1,-1],
             [44,-1,8,-1,-1,2,-1],
             [-1,30,-1,-1,-1,-1,-1],
             [3,-1,20,-1,46,6,-1],
             [-1,-1,-1,-1,-1,-1,29],
             [-1,29,21,33,-1,-1,-1]]
    
    print(Solution().snakesAndLadders(board))
