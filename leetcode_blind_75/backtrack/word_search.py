from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word_length = len(word)
        self.word = word
        self.board = board
        self.row = len(board)
        self.col = len(board[0])

        self.visited = set()
        found = False
        for cur_row in range(self.row):
            for cur_col in range(self.col):
                if board[cur_row][cur_col] == word[0]:
                    self.visited.add((cur_row,cur_col))
                    found = self.dfs(cur_row,cur_col,1)
                    if found:
                        return found
                    self.visited.remove((cur_row,cur_col))

        return found

    def dfs(self,cur_row,cur_col,cur_len):
        # print(cur_row,cur_col,cur_len)
        if cur_len == self.word_length:
            return True

        if cur_row+1 < self.row:
            if self.board[cur_row+1][cur_col] == self.word[cur_len] and (cur_row+1,cur_col) not in self.visited:
                self.visited.add((cur_row+1,cur_col))
                found = self.dfs(cur_row+1,cur_col,cur_len+1)
                self.visited.remove((cur_row+1,cur_col))
                if found:
                    return True

        if cur_row-1 >= 0:
            if self.board[cur_row-1][cur_col] == self.word[cur_len] and (cur_row-1,cur_col) not in self.visited:
                self.visited.add((cur_row-1,cur_col))
                found = self.dfs(cur_row-1,cur_col,cur_len+1)
                self.visited.remove((cur_row-1,cur_col))
                if found:
                    return True

        if cur_col+1 < self.col:
            if self.board[cur_row][cur_col+1] == self.word[cur_len] and (cur_row,cur_col+1) not in self.visited:
                self.visited.add((cur_row,cur_col+1))
                found = self.dfs(cur_row,cur_col+1,cur_len+1)
                self.visited.remove((cur_row,cur_col+1))
                if found:
                    return True

        if cur_col-1 >= 0:
            if self.board[cur_row][cur_col-1] == self.word[cur_len] and (cur_row,cur_col-1) not in self.visited:
                self.visited.add((cur_row,cur_col-1))
                found = self.dfs(cur_row,cur_col-1,cur_len+1)
                self.visited.remove((cur_row,cur_col-1))
                if found:
                    return True
        
        return False