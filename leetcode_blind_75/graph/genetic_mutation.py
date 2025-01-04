from collections import defaultdict,deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        gene_graph = defaultdict(list)

        for cur_gene in bank:
            diff_count = self.count_diff(startGene,cur_gene)
            if diff_count == 1:
                gene_graph[cur_gene].append(startGene)
                gene_graph[startGene].append(cur_gene)
                if cur_gene == endGene:
                    return 1

        for ind,cur_gene in enumerate(bank):
            for next_gene in bank[ind+1:]:
                diff_count = self.count_diff(next_gene,cur_gene)
                if diff_count == 1:
                    gene_graph[cur_gene].append(next_gene)
                    gene_graph[next_gene].append(cur_gene)

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
            for frnd in gene_graph[k]:
                if frnd not in visited:
                    if frnd == endGene:
                        return cur_level + 1
                    visited.add(frnd)
                    dq.append(frnd)
        return -1


        

    def count_diff(self,gene1,gene2):
        count = 0
        for char1, char2 in zip(gene1, gene2):
            if char1 != char2:
                count +=1
        return count