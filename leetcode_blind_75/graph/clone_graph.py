
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        clone_node = None
        dq = deque([node,-1])
        visited = set()
        node_map = dict()

        val = node.val
        temp_node = Node(val)
        node_map[node] = temp_node
        visited.add(node)
        while dq:
            k = dq.popleft()

            if k == -1 and not dq:
                break
            elif k == -1:
                dq.append(-1)
                continue
              
            
            new_node = node_map[k]
            if not clone_node: 
                clone_node = new_node
            
            
            for neighbor in k.neighbors:
                if node_map.get(neighbor) is None:
                    val = neighbor.val
                    temp_node = Node(val)
                    node_map[neighbor] = temp_node
                else:
                    temp_node = node_map[neighbor]

                new_node.neighbors.append(temp_node)

                if neighbor not in visited:
                    visited.add(neighbor)
                    dq.append(neighbor)
        
        return clone_node