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

        

    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.keys():
                return False
            cur_node = cur_node[char]
        return cur_node.get("is_word")
        

        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.keys():
                return False
            cur_node = cur_node[char]
        return True
