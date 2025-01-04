# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root,None])
        node_count = 0
        run_sum = 0
        ans = []
        while dq:
            k = dq.popleft()
            if not k and not dq:
                ans.append(run_sum/node_count)
                break
            if not k:
                ans.append(run_sum/node_count)
                node_count = 0
                run_sum = 0
                dq.append(None)
                continue
            node_count +=1
            run_sum += k.val
            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)
        return ans