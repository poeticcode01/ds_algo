from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.buildTrie([word])
        print(self.trie)
        self.ans_set = set()

        self.board = board
        self.board_row_cnt = len(board)
        self.board_col_cnt = len(board[0])
        self.found = False
        self.findWordSet()

        return self.found

    def findWordSet(self):
        for cur_row in range(self.board_row_cnt):
            for cur_col in range(self.board_col_cnt):
                if self.board[cur_row][cur_col] in self.trie.root.keys():
                    
                    temp = self.board[cur_row][cur_col]
                    if self.trie.root[temp]["is_word"] and temp not in self.ans_set:
                        self.ans_set.add(temp)
                        self.found = True
                        return 
            

                    self.board[cur_row][cur_col] = "#"
                    self.call_adjacent_cells(cur_row,cur_col,self.trie.root[temp],temp)
                    self.board[cur_row][cur_col] = temp

    def dfs(self,cur_row,cur_col,node,run_str):
        
        # print(cur_row,cur_col,"there",run_str)
        if cur_row >= self.board_row_cnt or cur_col >= self.board_col_cnt or cur_row < 0 or cur_col < 0 or self.found:
            return

        temp = self.board[cur_row][cur_col]

        if temp in node.keys():
            
            if node[temp]["is_word"] and run_str+temp not in self.ans_set:
                self.ans_set.add(run_str+temp)
                self.found = True
                return

            self.board[cur_row][cur_col] = "#"
            self.call_adjacent_cells(cur_row,cur_col,node[temp],run_str+temp)
            self.board[cur_row][cur_col] = temp

        return



    def call_adjacent_cells(self,row,col,node,run_str):
        
        # print(row,col,"here",run_str)
        self.dfs(row+1,col,node,run_str)
        self.dfs(row-1,col,node,run_str)
        self.dfs(row,col+1,node,run_str)
        self.dfs(row,col-1,node,run_str)

     

    def buildTrie(self,words):

        self.trie = Trie()
        for word in words:
            self.trie.insert(word)



class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self,word):
        node = self.root
        for cur_char in word:
            if cur_char not in node.keys():
                temp_dict = dict()
                temp_dict["is_word"] = False
                node[cur_char] = temp_dict
            node = node[cur_char]

        node["is_word"] = True