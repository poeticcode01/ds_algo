
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
            
        dq = deque([root,None])
        prv = None
        while dq:
            k = dq.popleft()
            if not k and not dq:
                break
            elif not k:
                dq.append(None)
                prv = None
                continue


            if k.left:
                dq.append(k.left)
            if k.right:
                dq.append(k.right)

            if prv:
                prv.next = k
            prv = k

        return root