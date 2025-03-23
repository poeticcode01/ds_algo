# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import List, Optional
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        while root:
            dq = deque([root])
            cur_leaf_nodes = []
            nodes = []
            while dq:
                k = dq.popleft()
                if self.is_leaf(k):
                    cur_leaf_nodes.append(k.val)
                    nodes.append(k)
                    continue
                
                lft = k.left
                is_lft_leaf = self.is_leaf(lft)
                rt = k.right
                is_rt_leaf = self.is_leaf(rt)
                if is_lft_leaf:
                    k.left = None

                if is_rt_leaf: 
                    k.right = None
                if lft:
                    dq.append(lft)
                if rt:
                    dq.append(rt)

            # print(cur_leaf_nodes)
            if cur_leaf_nodes:
                ans.append(cur_leaf_nodes)
            if len(cur_leaf_nodes) == 1 and nodes[0] == root:
                break

        return ans


                

    def is_leaf(self,node):
        if not node:
            return True

        if not node.left and not node.right:
            return True

        return False