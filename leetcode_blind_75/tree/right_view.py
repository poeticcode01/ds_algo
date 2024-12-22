# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        dq = deque([root,None])
        ans = []
        level = 0
        while dq:
            k = dq.popleft()
            if not k and dq:
                level+=1
                dq.append(None)
                continue
            elif not k:
                break

            if not dq[0]:
                ans.append(k.val)
            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)
        return ans