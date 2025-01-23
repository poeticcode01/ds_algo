from collections import defaultdict,deque
from typing import List



class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        gene_set = set(bank)
        # print(gene_graph)
        dq = deque([startGene, None])
        cur_level = 0
        visited = set()
        visited.add(startGene)
        while dq:
            k = dq.popleft()
            if not k and not dq:
                return -1
            if not k:
                cur_level +=1
                dq.append(None)
                continue
            if k == endGene:
                return cur_level
            for ind, itm in enumerate(k):
                for gene_char in "ACGT":
                    temp_gene = k[:ind] + gene_char + k[ind+1:]
                    if temp_gene in gene_set and temp_gene not in visited:
                        if temp_gene == endGene:
                            return cur_level + 1
                        visited.add(temp_gene)
                        dq.append(temp_gene)
                
        return -1