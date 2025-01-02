# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []

        stck = [root]
        k = root.left
        while stck or k:
            if not k:
                temp = stck.pop()
                self.inorder.append(temp.val)
                k = temp.right
            else:
                stck.append(k)
                k = k.left

        self.cur_ind = 0
        self.node_count = len(self.inorder)

        # print("init",self.inorder,self.cur_ind)
        

    def next(self) -> int:
        # print("next", self.inorder,self.cur_ind)
        temp = self.inorder[self.cur_ind]
        self.cur_ind +=1
        return temp
           

    def hasNext(self) -> bool:
        return self.cur_ind < self.node_count