# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prv = None
        is_inorder = self.inorder(root)
        return is_inorder

    def inorder(self,root):
        if not root:
            return True
        if not root.left and not root.right:
            if self.prv is None:
                self.prv = root.val 
                return True
            if root.val > self.prv:
                self.prv = root.val
                # print("here")
                return True
            else:
                return False
        lft = self.inorder(root.left)
        if not lft:
            return False
        if  self.prv is None:
            self.prv = root.val

        elif root.val > self.prv:
            self.prv = root.val
        else:
            return False
        rt = self.inorder(root.right)
        if not rt:
            return False
        return True