from collections import defaultdict,deque
from typing import List
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        process_graph = defaultdict(list)
        for ind, itm in enumerate(ppid):
            process_graph[itm].append(pid[ind])
        kill_list = []
        dq = deque([kill])
        while dq:
            kill = dq.popleft()
            kill_list.append(kill)
            for child in process_graph[kill]:
                dq.append(child)

        return kill_list