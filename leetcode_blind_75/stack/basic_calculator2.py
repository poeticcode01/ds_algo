class Solution:
    def calculate(self, s: str) -> int:
        cur = prv = res = 0
        i = 0
        cur_op = "+"
        while i < len(s):
            cur_char = s[i]
            if cur_char.isdigit():
                while  i < len(s) and s[i].isdigit():
                    cur = cur*10 + int(s[i])
                    i +=1
                i -=1

                if cur_op == "+":
                    res = res + cur
                    prv = cur
                elif cur_op  == "-":
                    res = res - cur
                    prv = -cur
                elif cur_op == "*":
                    res = res - prv
                    res = res + (prv*cur)
                    prv = prv*cur
                else:
                    res = res - prv
                    res = res + int(prv/cur)
                    prv = int(prv/cur)
                cur = 0
            elif cur_char != " ":
                cur_op = cur_char

            i+=1

        return res