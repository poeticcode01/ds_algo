from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        self.getCandidateSum(candidates, "", 0,target)
        
            
        return list(self.ans)

    def getCandidateSum(self,candidates, run_str, run_sum, target):
        

        for cur_val in candidates:
            temp = sorted(run_str+str(cur_val))
            if cur_val + run_sum == target:
                
                if temp  not in  self.ans:
                    self.ans.append(temp)
               
                return
            elif cur_val + run_sum < target:
                self.getCandidateSum(candidates, temp, cur_val + run_sum, target)
            else:
                return