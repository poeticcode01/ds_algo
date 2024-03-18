# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.merge(preorder,inorder)

    def merge(self,preorder,inorder):
        root_itm = preorder[0]
        root_node = TreeNode(root_itm)

        search_ind = self.search(root_itm,inorder)
        

        if search_ind != 0:
            lft_preorder = preorder[1:1+search_ind]
            root_node.left = self.merge(lft_preorder,inorder[:search_ind])
        if search_ind != len(inorder) - 1:
            rt_preorder = preorder[search_ind+1:]
            root_node.right = self.merge(rt_preorder,inorder[search_ind+1:])
        return root_node
        
        


    def search(self,key,search_lst):
        for ind ,itm in enumerate(search_lst):
            if itm == key:
                return ind
        return None