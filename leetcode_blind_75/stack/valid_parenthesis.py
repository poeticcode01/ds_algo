class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = set(["(","{","["])
        match_braces = {
                        ")": "(",
                        "}": "{",
                        "]": "["
                        }
        stck = []
        for itm in s:
            if itm in open_braces:
                stck.append(itm)
            else:
                if not stck:
                    return False
                k = stck.pop()
                # print(k)
                if match_braces[itm] != k:
                    return False

        if len(stck) > 0:
            return False
        return True