from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isEqual(p,q)
        
    def isEqual(self,p,q):
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False

        if p.val != q.val:
            return False

        lft = self.isEqual(p.left,q.left)
        if not lft:
            return False

        rt = self.isEqual(p.right,q.right)
        if not rt:
            return False
            
        return True