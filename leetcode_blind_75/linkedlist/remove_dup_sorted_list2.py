# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        cur = head

        while cur:
            if cur.next and cur.next.val == cur.val:
                dup = cur.next
                cur_prv = cur
                while dup and dup.val == cur.val:
                    cur_prv = dup
                    dup = dup.next

                if dup:
                    nxt = dup
                if prv:
                    prv.next = dup
                else:
                    head = dup
                    cur_prv.next = None
                cur = dup
            else:
                prv = cur
                cur = cur.next

        return head