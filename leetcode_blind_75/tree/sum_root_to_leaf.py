# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        self.dfs(root,0)
        return self.total_sum

    def dfs(self,node,run_sum):
        if not node:
            self.total_sum += run_sum
            return 
        if not node.left and not node.right:
            self.total_sum += run_sum*10+node.val
            return
        
        if node.left:
            self.dfs(node.left,run_sum*10+node.val)
        if node.right:
            self.dfs(node.right,run_sum*10+node.val)