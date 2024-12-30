# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        flatten_head = None
        
    
        stck = []
        k = root
        while k or stck:
            temp = None
            if k:
                # print(k.val)
                temp = k
                stck.append(k)
                k = k.left
            else:
                k = stck.pop()
                k = k.right

            if temp:
                # print(temp.val)
                if flatten_head:
                    run_node.left = temp
                    run_node = run_node.left
                else:
                    flatten_head = temp
                    run_node = flatten_head
                    
        cur_node = flatten_head
        while cur_node:
            temp = cur_node
            cur_node.right = cur_node.left
            cur_node.left = None
            cur_node = cur_node.right
        return flatten_head