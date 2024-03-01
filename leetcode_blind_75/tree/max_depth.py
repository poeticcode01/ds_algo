from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        cur_depth = 1
        return self.getMaxDepth(root,cur_depth)
    def getMaxDepth(self, node,cur_depth):
        ans = cur_depth
        if node.left:
            ans = max(ans,self.getMaxDepth(node.left,cur_depth+1))
        if node.right:
            ans = max(ans,self.getMaxDepth(node.right,cur_depth+1))
        return ans
