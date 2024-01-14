class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        found = False
        cur = head
        while cur and not found:
            if cur in node_set:
                found = True
                break
            node_set.add(cur)
            cur = cur.next
        return found