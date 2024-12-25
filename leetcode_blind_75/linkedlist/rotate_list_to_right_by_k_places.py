# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        orig_node_cnt = 0
        cur = head
    
        while cur:
            orig_node_cnt +=1
            cur = cur.next

        if k == orig_node_cnt:
            return head
        elif k > orig_node_cnt:
            k = k%orig_node_cnt

        if k == 0:
            return head




        prv = None
        cur = head
        kth_node = head
        node_cnt =0 
        while cur:
            node_cnt +=1
            if node_cnt <= k:
                end = cur
                cur = cur.next

                continue
            else:
                node_cnt = k
                prv = kth_node
                kth_node = kth_node.next
                end = cur
                cur = cur.next

        
        prv.next = None
        end.next = head
        head = kth_node

        return head