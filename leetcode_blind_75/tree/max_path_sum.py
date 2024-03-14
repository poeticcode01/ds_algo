import sys
from typing import Optional
sys.setrecursionlimit(1000006)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        self.maxSum(root)
        return self.ans
    def maxSum(self,root):
        if not root:
            return 0
        root_val = root.val
        max_sum = root_val
        lft = self.maxSum(root.left)
        rt = self.maxSum(root.right)
        max_sum = max(max_sum,root_val+lft)
        max_sum = max(max_sum,root_val+rt)
        tmp = max(max_sum,root_val+rt+lft)
        self.ans = max(self.ans,tmp)
        return max_sum