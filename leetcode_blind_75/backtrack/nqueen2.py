class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        
        self.board = []
        self.board_size = n

        for i in range(self.board_size):
            temp = [False for j in range(n)]
            self.board.append(temp)
        
        self.ans = 0

        self.backtrack(0)
        return self.ans

    def backtrack(self,cur_row):
        if cur_row >= self.board_size:
            # print(self.board)
            self.ans +=1
            return
        ans_before = self.ans
        for cur_col in range(self.board_size):
            self.board[cur_row][cur_col] = True
            if self.isQueenPlacable(cur_row, cur_col):
                self.backtrack(cur_row+1)
                if cur_row == 0:
                    if self.ans > ans_before:
                        # print("inside" ,self.board)
                        ans_before = self.ans
                    

            self.board[cur_row][cur_col] = False

        return
            

    def isQueenPlacable(self,cur_row, cur_col):
        

        # check current row
        for col_pos in range(self.board_size):
            if col_pos == cur_col:
                continue

            if self.board[cur_row][col_pos]:
                # if self.board[0][2]:
                    # print("cehck",self.board)

                return False

        # check curent col
        for row_pos in range(self.board_size):
            if row_pos == cur_row:
                continue
            if self.board[row_pos][cur_col]:
                # if self.board[0][2]:
                    # print("cehck",self.board)
                return False
        
        # check diagonal upper right
        rt_col_pos = cur_col + 1
        for i in range(cur_row-1,-1,-1):
            if rt_col_pos >= self.board_size:
                break
            if self.board[i][rt_col_pos]:
                # if self.board[0][2]:
                    # print("cehck",self.board)
                return False
            rt_col_pos +=1

        # check diagonal lower right
        rt_col_pos = cur_col + 1
        for i in range(cur_row+1,self.board_size):
            if rt_col_pos >= self.board_size:
                break
            if self.board[i][rt_col_pos]:
                # if self.board[0][2]:
                    # print("cehck",self.board)
                return False
            rt_col_pos +=1

        # check diagonal upper left
        lft_col_pos = cur_col - 1
        for i in range(cur_row-1,-1,-1):
            if lft_col_pos < 0:
                break
            if self.board[i][lft_col_pos]:
                # if self.board[0][2]:
                    # print("cehck upper left",self.board)
                return False
            lft_col_pos -=1

        # check diagonal lower left
        lft_col_pos = cur_col - 1
        for i in range(cur_row+1,self.board_size):
            if lft_col_pos < 0:
                break
            if self.board[i][lft_col_pos]:
                # if self.board[0][2]:
                    # print("cehck lower left",self.board)
                return False
            lft_col_pos -=1

        return True