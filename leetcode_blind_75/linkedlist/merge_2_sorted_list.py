from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNoteBook], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        head = None
        run_node = None
        while cur1 and cur2:
            if cur1.val < cur2.val:
                if not head:
                    head = cur1
                    run_node = cur1
                else:
                    run_node.next = cur1
                    run_node = cur1
                cur1 = cur1.next
    
            else:
                if not head:
                    head = cur2
                    run_node = cur2
                else:
                    run_node.next = cur2
                    run_node = cur2
                cur2 = cur2.next

        if cur1:
            if not head:
                head = cur1
                run_node = cur1
            else:
                run_node.next = cur1
        if cur2:
            if not head:
                head = cur2
                run_node = cur2
            else:
                run_node.next = cur2

        return head