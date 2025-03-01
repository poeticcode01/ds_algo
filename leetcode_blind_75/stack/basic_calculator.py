class Solution:
    def calculate(self, s: str) -> int:
        cur=res=0
        sign=1
        stck = []
        for char in s:
            if char.isdigit():
                cur = cur*10 + int(char)
            elif char in ["+","-"]:
                # print(type(res),type(sign),type(cur))
                res =  res + (sign*cur)
                sign = 1 if char == "+" else -1
                cur = 0
            elif char == "(":
                stck.append(res)
                stck.append(sign)
                res = 0
                cur = 0
                sign = 1
            elif char == ")":
                res = res + sign*cur
                sign = stck.pop()
                res = sign*res
                prev = stck.pop()
                res = res + prev
                cur = 0 
                sign =1
        return res + sign*int(cur)