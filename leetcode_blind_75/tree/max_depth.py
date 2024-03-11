from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.getMaxDepth(root)
    def getMaxDepth(self, node):
        ans = 1
        lft,rt = 1,1
        if node.left:
            lft = 1 + self.getMaxDepth(node.left)
        if node.right:
            rt = 1 + self.getMaxDepth(node.right)
        ans = max(lft,rt)
        return ans
