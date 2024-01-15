from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        prev = None
        cur = head
        nxt = cur.next if cur else None
        while cur:
            cur.next = prev
            prev = cur
            cur = nxt
            if cur:
                nxt = cur.next
            else:
                nxt = None
        return prev
    