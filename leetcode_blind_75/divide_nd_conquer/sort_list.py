# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        return self.merge_sort(head)


    def merge_sort(self, head):
        slow = head
        fast = head.next
        if not fast:
            return slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = slow.next
        slow.next = None
        # print("before",head,head2)

        head1 = self.merge_sort(head)
        head2 = self.merge_sort(head2)
        # print("after",head1,head2)
        return self.merge(head1,head2)



    

    def merge(self, head1, head2):
        # print()

        new_head = None
        run_node = None

        while head1 and head2:
            if head1.val <= head2.val:
                if not new_head:
                    new_head = head1
                    run_node = new_head
                else:
                    run_node.next = head1
                    run_node = head1

                temp = head1.next
                head1.next = None
                head1 = temp

            else:
                if not new_head:
                    new_head = head2
                    run_node = new_head
                else:
                    run_node.next = head2
                    run_node = head2

                temp = head2.next
                head2.next = None
                head2 = temp

        while head1:
            if not new_head:
                new_head = head1
                run_node = new_head
            else:
                run_node.next = head1
                run_node = head1

            temp = head1.next
            head1.next = None
            head1 = temp

            
        
        while head2:
            if not new_head:
                new_head = head2
                run_node = new_head
            else:
                run_node.next = head2
                run_node = head2

            temp = head2.next
            head2.next = None
            head2 = temp

        # print("merge",new_head)
        return new_head