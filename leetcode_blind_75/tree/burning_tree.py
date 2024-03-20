# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict,deque
from typing import Optional
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.edge_list = defaultdict(list)
        self.dfs(root)
        visited = set()
        visited.add(start)
        ans = 0
        cur_level = 0
        dq = deque([start,-1])
        while dq:
            k = dq.popleft()
            if k == -1 and not dq:
                break
            elif k == -1:
                cur_level +=1
                dq.append(-1)
                continue
            for frnd in self.edge_list[k]:
                if frnd in visited:
                    continue
                visited.add(frnd)
                dq.append(frnd)
        return max(ans,cur_level)


    def dfs(self,root):
        if not root:
            return
        if root.left:
            self.edge_list[root.val].append(root.left.val)
            self.edge_list[root.left.val].append(root.val)
            self.dfs(root.left)
        if root.right:
            self.edge_list[root.val].append(root.right.val)
            self.edge_list[root.right.val].append(root.val)
            self.dfs(root.right)
        return 
        