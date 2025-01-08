# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root, None])
        switch = False
        ans = []
        cur_level = []
        while dq:
            k = dq.popleft()
            if not k and not dq:
                if not switch:
                    ans.append(cur_level)
                else:
                    ans.append(list(reversed(cur_level)))
                break
            elif not k:
                if not switch:
                    ans.append(cur_level)
                else:
                    ans.append(list(reversed(cur_level)))
                switch = not switch
                cur_level = []

                dq.append(None)
                continue

            cur_level.append(k.val)
            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)

        return ans