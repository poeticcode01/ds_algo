from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.get_permutation(nums,[])

        return self.ans


    def get_permutation(self, left_to_choose,run_permutation):
        if not left_to_choose:
            if run_permutation:
                self.ans.append(run_permutation)
            return

        for ind, itm in enumerate(left_to_choose):
            self.get_permutation(left_to_choose[:ind]+left_to_choose[ind+1:],run_permutation+[itm])