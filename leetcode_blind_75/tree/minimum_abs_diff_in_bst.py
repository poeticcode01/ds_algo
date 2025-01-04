# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stck = [root]
        k = root.left
        last_val = None
        min_ans = None
        while stck or k:
            if k:
                stck.append(k)
                k = k.left
            else:
                temp = stck.pop()
                if last_val is not None:
                    if min_ans:
                        min_ans = min(min_ans,abs(temp.val-last_val))
                    else:
                        min_ans = abs(temp.val-last_val)

                last_val = temp.val
                k = temp.right
        return min_ans