# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left,root.right)


    def dfs(self,lft, rt):
        if (lft and not rt) or (not lft and rt) :
            return False

        if not lft and not rt:
            return True

        if lft.val != rt.val:
            return False

        part1 = self.dfs(lft.left,rt.right)
        if not part1:
            return False
        part2 = self.dfs(lft.right,rt.left)
        return part2