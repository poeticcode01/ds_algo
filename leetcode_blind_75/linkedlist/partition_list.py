# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head :
            return head

        lft_strt = None
        rt_strt = None
        cur_lft = None
        cur_rt = None

        cur = head
        while cur:
            if cur.val < x:
                if not lft_strt:
                    lft_strt = cur
                    lft = cur
                
                else:
                    lft.next = cur
                    lft = lft.next
                
            else:
                if not rt_strt:
                    rt_strt = cur
                    rt = cur
                
                else:
                    rt.next = cur
                    rt = rt.next
                
            temp = cur.next
            cur.next = None
            cur = temp

        if not lft_strt:
            return rt_strt

        lft.next = rt_strt

        return lft_strt