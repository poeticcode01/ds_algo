# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = False
        self.dfs(root,p,q)
        return self.lca

    def dfs(self,node,p,q):

        if not node:
            return False,False

        found_p =   False
        found_q = False

        if node == p:
            found_p = True
            # print("found p",node.val)

        if node == q:
            found_q = True
            

        if not found_p or not found_q:
            left_found_p ,left_found_q = self.dfs(node.left,p,q)
        if self.lca:
            return True , True
        found_p = found_p or left_found_p
        found_q = found_q or left_found_q

        if not found_p or not found_q:
            right_found_p ,right_found_q = self.dfs(node.right,p,q)

        found_p = found_p or right_found_p
        found_q = found_q or right_found_q


        if found_p and found_q:
            # print("found",node.val)
            if not self.lca:
                self.lca = node
        return found_p,found_q

