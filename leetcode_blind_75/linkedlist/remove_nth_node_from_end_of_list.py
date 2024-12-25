# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prv = head
        cur = head 
        nth_node = head
        run_cnt = 0

        while cur:
            run_cnt +=1 
            cur = cur.next
            if run_cnt <= n:       
                continue
            else:
                prv = nth_node
                nth_node = nth_node.next
                run_cnt = n

        if nth_node == head:
            head = nth_node.next
        else:
            prv.next = nth_node.next
            nth_node.next = None

        return head