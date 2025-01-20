class Solution:
    def calculate(self, s: str) -> int:
        stck = []
        res=cur=0
        sign = 1
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            elif char in ["+","-"]:
                res = res + sign*cur
                sign = 1 if char == "+" else -1
                cur = 0
            elif char == "(":
                stck.append(res)
                stck.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign*cur
                res *= stck.pop()
                res += stck.pop()
                cur = 0
                sign = 1
        return res + sign*cur