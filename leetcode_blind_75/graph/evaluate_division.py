from collections import defaultdict
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        weighted_graph = defaultdict(list)
        for eq, val in zip(equations,values):
            a,b = eq
            weighted_graph[a].append((b,val))
            weighted_graph[b].append((a,1/val))

        

        def bfs(strt,end):
            if strt not in weighted_graph or end not in weighted_graph:
                return -1.0

            dq = deque([(strt,1)])
            visited = set()
            
            while dq:
                temp, prod = dq.popleft()
                if temp == end:
                    return prod

                visited.add(temp)

                for neighbor,val in weighted_graph[temp]: 
                    if neighbor not in visited:
                        dq.append((neighbor,prod*val))

            return -1
        ans = []
        for var1,var2 in queries:
            ans.append(bfs(var1,var2))

        return ans
                