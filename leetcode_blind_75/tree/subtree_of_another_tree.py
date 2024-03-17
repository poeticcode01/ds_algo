# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        dq = deque([root,None])
        
        while dq:
            k = dq.popleft()
            if not k and not dq:
                break
            elif not k:
                dq.append(None)
                continue
            is_equal = self.isEqual(k,subRoot)
            if is_equal:
                return True

            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)
             

    def isEqual(self,p,q):
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False

        if p.val != q.val:
            return False

        lft = self.isEqual(p.left,q.left)
        if not lft:
            return False

        rt = self.isEqual(p.right,q.right)
        if not rt:
            return False
            
        return True
        