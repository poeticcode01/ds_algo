# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) != len(postorder):
            return None

        return self.dfs(inorder,postorder)

    def dfs(self,inorder,postorder):
        if not inorder:
            return None

        ln = len(inorder)

        root_node = TreeNode(postorder[-1])
        ind = self.search(inorder,postorder[-1])

        root_node.left = self.dfs(inorder[:ind],postorder[:ind])
        root_node.right = self.dfs(inorder[ind+1:],postorder[ind:ln-1])

        return root_node


    def search(self, inorder, val):

        for ind, itm in enumerate(inorder):
            if itm == val:
                return ind