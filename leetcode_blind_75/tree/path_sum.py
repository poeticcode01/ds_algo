# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        run_sum = 0
        self.dfs(root,run_sum,targetSum)
        return self.found

    def dfs(self,root,run_sum,targetSum):
        if not root:
            return
        if not root.left and not root.right:
            temp = run_sum + root.val
            if temp == targetSum:
                self.found = True
            return
        self.dfs(root.left,run_sum+root.val,targetSum)
        if self.found:
            return
        self.dfs(root.right,run_sum+root.val,targetSum)
        return