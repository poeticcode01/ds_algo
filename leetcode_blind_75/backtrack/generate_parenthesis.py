from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.length = n
        self.ans = []
        self.allPossibleParenthesis("",0,0)

        return self.ans

    def allPossibleParenthesis(self,run_parenthesis,open,close):
        if open == self.length and close == self.length:
            self.ans.append(run_parenthesis)
            return
        
        if close > open or close > self.length or open > self.length:
            return
        else:
            self.allPossibleParenthesis(run_parenthesis+"(",open+1,close)
            self.allPossibleParenthesis(run_parenthesis+")",open,close+1)