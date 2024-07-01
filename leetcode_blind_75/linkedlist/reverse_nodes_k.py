from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # strt
        # end
        # prv 
        # nxt

        #new_head update

        #pos

        

        cur = head
        lft_prv = None
        rt_nxt = None

        while cur:
            pos = 1
            lft = None
            rt = None
            
            while cur and pos <= k:
                if pos == 1:
                    lft = cur
                if pos == k or cur.next is None:
                    rt = cur
                    rt_nxt = cur.next
                cur = cur.next
                pos +=1

            if lft_prv:
                lft_prv.next = None
            
            rt.next = None

            if pos > k:
                self.reverse(lft)

                if lft_prv is None:
                    head = rt

                else:
                    lft_prv.next = rt


                lft_prv = lft
                cur = rt_nxt
            else:
                lft_prv.next = lft


        return head

    def reverse(self,lft):

        prv = None
        cur = lft
        nxt = cur.next

        while cur:
            cur.next = prv
            prv = cur
            cur = nxt
            if nxt:
                nxt = nxt.next