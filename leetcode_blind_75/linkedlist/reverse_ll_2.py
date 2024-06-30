# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lft_prv = None
        rt_nxt = None

        lft = None
        rt = None

        cur = head
        prv = None
        pos = 1
        while cur:
            # print(prv,pos)
            if pos == left:
                # print(pos,prv,prv.val)
                # print(prv.val,cur.val)
                lft = cur
                lft_prv = prv
                # print(pos,cur.val)
                # print(lft_prv.val)
                
            if pos == right:
                rt = cur
                rt_nxt = cur.next

            pos +=1
            prv = cur
            # print(prv.val,pos)
            cur = cur.next

        if lft_prv:
            lft_prv.next = None

        if rt_nxt:
            rt.next = None

        # print(lft_prv,rt_nxt)
        self.reverse(lft,rt)
        # print(lft,rt)
        # print(lft.val,rt.val)
        # print(lft_prv.val)
        if lft_prv:
            lft_prv.next = rt
        else:
            head = rt
        
        lft.next = rt_nxt
        return head

    def reverse(self,lft,rt):
        prv = None
        cur = lft
        nxt = cur.next
        
        while cur:
            cur.next = prv
            prv = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
            