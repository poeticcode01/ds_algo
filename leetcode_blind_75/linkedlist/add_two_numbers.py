# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = None
        k1 = l1
        k2 = l2

        carry = 0
        while k1 or k2 or carry:
            a = 0
            b = 0

            if k1:
                a = k1.val
                k1 = k1.next
            
            if k2:
                b = k2.val
                k2 = k2.next

            val = (a + b + carry)%10
            carry = (a + b + carry)//10

            if not sum_head:
                sum_head = ListNode(val)
                run_ptr = sum_head
            else:
                temp = ListNode(val)
                run_ptr.next = temp
                run_ptr = run_ptr.next
        
        

        print(sum_head.val)

        return sum_head