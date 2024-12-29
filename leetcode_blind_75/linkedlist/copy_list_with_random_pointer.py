
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        clone_head = None
        
        orig_clone_node_map = {}

        cur_node = head
        while cur_node:
            temp = Node(cur_node.val)

            if not clone_head:
                clone_head = temp
                run_node = clone_head

            else:
                run_node.next= temp
                run_node = run_node.next

            orig_clone_node_map[cur_node] = run_node
            cur_node = cur_node.next

        cur_node = head
        while cur_node:
            orig_random_node = cur_node.random
            if orig_random_node is None:
                cur_node = cur_node.next
                continue

            clone_node = orig_clone_node_map[cur_node]
            clone_random_node = orig_clone_node_map[orig_random_node]
            clone_node.random = clone_random_node

            cur_node = cur_node.next

        return clone_head