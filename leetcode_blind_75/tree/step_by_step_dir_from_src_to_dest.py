from collections import defaultdict
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.graph = defaultdict(list)
        self.dfs(root)
        visited = set()
        dq = deque([(startValue,"")])
        visited.add(startValue)

        print(self.graph)
        
        while dq:
            k = dq.popleft()
            # print(k)
            for frnd in self.graph[k[0]]:
                # print("in",frnd)
                if frnd[0] in visited:
                    continue
                if frnd[0] == destValue:
                    return k[1]+frnd[1]
                else:
                    dq.append((frnd[0],k[1]+frnd[1]))
                    visited.add(frnd[0])



    def dfs(self,node):
        if not node:
            return
        if node.left:
            self.graph[node.val].append((node.left.val,"L"))
            self.graph[node.left.val].append((node.val,"U"))
            self.dfs(node.left)
        if node.right:
            self.graph[node.val].append((node.right.val,"R"))
            self.graph[node.right.val].append((node.val,"U"))
            self.dfs(node.right)