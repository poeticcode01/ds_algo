from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        candidates = sorted(candidates)
        self.getCandidateSum(candidates, [], target)
        self.final_ans = []
        for ans_str in self.ans:
            temp = ans_str.split(",")
            temp = [int(num) for num in temp]
            self.final_ans.append(temp)

        return self.final_ans

    def getCandidateSum(self,candidates, run_list, target):
        cur_sum = 0
        if len(run_list) > 0:
            cur_sum = sum(run_list)

        for cur_val in candidates:
            temp1 = sorted(run_list+[cur_val])
            temp2 = [str(num) for num in temp1]
            temp3 = ",".join(temp2)
            if cur_val + cur_sum == target:
                
                if temp3  not in  self.ans:
                    self.ans.add(temp3)
               
                return
            elif cur_val + cur_sum < target:
                self.getCandidateSum(candidates, temp1, target)
            else:
                return