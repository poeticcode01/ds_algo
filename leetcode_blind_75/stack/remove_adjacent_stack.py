class Solution:
    def removeDuplicates(self, s: str) -> str:
        stck = [s[0]]
        i = 1
        while i < len(s):
            if len(stck) >=1:
                if s[i] == stck[-1]:
                    stck.pop()
                    i +=1
                    continue
                
                
            stck.append(s[i])
            i +=1
        return "".join(stck)