class WordDictionary:

    def __init__(self):
        self.root = dict()
        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.keys():
                cur_node[char] = dict()
            cur_node = cur_node[char]
        cur_node["is_word"] = True
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        for ind,char in enumerate(word):
            if char == ".":
                for key in cur_node.keys():
                    if key == "is_word":
                        continue
                    found = self.dfs(word[ind+1:],cur_node[key])
                    if found:
                        return True
                return False
            if char not in cur_node.keys():
                return False
            cur_node = cur_node[char]
        return cur_node.get("is_word")

    def dfs(self,word,node):
        for ind,char in enumerate(word):
            if char == ".":
                for key in node.keys():
                    if key == "is_word":
                        continue
                    found = self.dfs(word[ind+1:],node[key])
                    if found:
                        return True
                return False
            else:
                if char not in node.keys():
                    return False
            node = node[char]
        # print(node)
        return node.get("is_word")