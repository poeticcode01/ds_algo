# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.recur_lca(root,p,q)

        return self.lca

    def recur_lca(self,root,p,q):
        if not root:
            return False
        if self.lca:
            return True
        cur_node = (root == p) or (root == q)
        lft = self.recur_lca(root.left,p,q)
        if self.lca:
            return True
        rt = self.recur_lca(root.right,p,q)

        if lft and rt or (lft and cur_node) or (rt and cur_node):
            if not self.lca:
                self.lca = root
        
        if lft or rt or cur_node:
            return True
        return False