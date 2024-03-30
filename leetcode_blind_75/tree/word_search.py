from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for each_word in words:
            trie.insert(each_word)
        
        root = trie.root
        self.visit_set = set()
        self.board = board
        self.row_cnt = len(board)
        self.col_cnt = len(board[0])
        
        self.ans_set = set()
        # print(root.keys())
        for row in range(self.row_cnt):
            for col in range(self.col_cnt):
                itm =  board[row][col]
                if itm not in root.keys():
                    continue
                board[row][col] = "#"
                # self.visit_set.add((row,col))
                self.dfs((row,col),root[itm],itm)
                board[row][col] = itm

        return list(self.ans_set)

    def dfs(self,cell,node,run_word):
        if node.get("is_word"):
            if run_word not in self.ans_set:
                self.ans_set.add(run_word)
                # self.ans.append(run_word)
        cur_row = cell[0]
        cur_col = cell[1]
        neighbors_list = [(cur_row,cur_col-1),(cur_row,cur_col+1),(cur_row+1,cur_col),(cur_row-1,cur_col)]
        for neighbrs in neighbors_list:
            
            # if (row,col) in self.visit_set:
            #     continue
            row = neighbrs[0]
            col = neighbrs[1]

            if row < 0 or row >= self.row_cnt or col < 0 or col >= self.col_cnt:
                continue
            itm = self.board[row][col]
            if itm == "#":
                continue

            if itm not in node.keys():
                continue
            # self.visit_set.add((row,col))
            self.board[row][col] = "#"
            self.dfs((row,col),node[itm],run_word+itm)
            # self.visit_set.remove((row,col))
            self.board[row][col] = itm



class Trie:

    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.keys():
                cur_node[char] = dict()
            cur_node = cur_node[char]
        cur_node["is_word"] = True

if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    Solution().findWords(board,words)