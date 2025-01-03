# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        dq = deque([root,None])
        cur_level = 0
        nextlevel_child = False
        ans = 0
        while dq:
            k = dq.popleft()
            if not k and not dq:
                break
            elif not k:
                if not nextlevel_child:
                    ans += len(dq)
                    break
                dq.append(None)
                

                nextlevel_child = False
                continue
            ans +=1
            if k.left:
                dq.append(k.left)
                if k.left.left:
                    nextlevel_child = True
            if k.right:
                if k.right.left:
                    nextlevel_child = True
                dq.append(k.right)

        return ans