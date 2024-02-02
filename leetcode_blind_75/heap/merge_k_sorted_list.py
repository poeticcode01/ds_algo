# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from tkinter.tix import ListNoteBook
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNoteBook]]) -> Optional[ListNode]:
        heap_data = []
        cnt = 0
        for cur_lst in lists:
            if not cur_lst:
                continue
            cnt +=1
            heapq.heappush(heap_data,(cur_lst.val,cnt,cur_lst))

        head = None
        run_node = None
        while heap_data:
            k = heapq.heappop(heap_data)
            if not head:
                head = k[2]
                run_node = head
            else: 
                run_node.next = k[2]
                run_node = k[2]
            
            if k[2].next:
                cnt +=1
                heapq.heappush(heap_data,(k[2].next.val,cnt,k[2].next))
        return head

        