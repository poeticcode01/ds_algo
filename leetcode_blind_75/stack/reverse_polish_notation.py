from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_operator_set  = set(["+","-","*","/"])
        stck = []
        for itm in tokens:
            if itm in valid_operator_set:
                a = stck.pop()
                b = stck.pop()
                if itm == "/":
                    
                    temp = abs(b)//abs(a)
                    if temp == 0:
                        stck.append(temp)
                    else:
                        if (b < 0 and  not (a < 0)) or (a < 0 and  not (b < 0)):
                            stck.append(-temp)
                        else:
                            stck.append(temp)

                    
                elif itm == "-":
                    temp = b - a
                    stck.append(temp)
                elif itm == "*":
                    temp = a * b
                    stck.append(temp)
                else:
                    temp = a + b
                    stck.append(temp)
            else:
                # print(int(itm))
                stck.append(int(itm))
        # print(stck)
        return stck.pop()