from ast import List
from collections import deque
from typing import Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        dq = deque([root,None])
        cur_level = []
        while dq:
            k = dq.popleft()
            if not k and not dq:
                ans.append(cur_level)
                break
            elif not k:
                dq.append(None)
                ans.append(cur_level)
                cur_level = []
                continue
            cur_level.append(k.val)
            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)

        return ans