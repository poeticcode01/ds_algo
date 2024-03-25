# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = None
        self.ind = 0
        self.smallest_key = k
        self.inorder_traversal(root)
        return self.ans

    def inorder_traversal(self,root):
        if not root:
            return False
        lft = self.inorder_traversal(root.left)
        if lft:
            return True
        self.ind +=1
        if self.ind == self.smallest_key:
            self.ans = root.val
            return True
        rt = self.inorder_traversal(root.right)
        return rt