from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.get_combinations(k,[],1,n)

        return self.ans


    def get_combinations(self,left_to_choose,run_combination,choice,n):
        if left_to_choose == 0:
            if run_combination:
                self.ans.append(run_combination)
            return

        for itm in range(choice,n+1):
            self.get_combinations(left_to_choose-1,run_combination+[itm],itm+1,n)