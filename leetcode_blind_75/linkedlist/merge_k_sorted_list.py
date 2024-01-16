import heapq
from tkinter.tix import ListNoteBook
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNoteBook]]) -> Optional[ListNode]:
        heap_list = []
        counter = 1
        for cur_lst in lists:
            if cur_lst:
                heapq.heappush(heap_list,(cur_lst.val,counter,cur_lst))
                counter+=1
        head = None
        run_node = None
        while heap_list:
            temp_val,temp_cntr,temp_node = heapq.heappop(heap_list)
            if not head:
                head = temp_node
                run_node = temp_node
            else:
                run_node.next = temp_node
                run_node = temp_node
            if temp_node.next:
                heapq.heappush(heap_list,(temp_node.next.val,counter,temp_node.next))
                counter +=1
            else:
                continue
        return head