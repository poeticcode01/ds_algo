from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertChild(root)
    def invertChild(self, root):
        if not root:
            return None
        temp = root.left
        root.left = self.invertChild(root.right)
        root.right = self.invertChild(temp)
        return root
        