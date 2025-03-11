class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stck = []
        special_char_set = set([".",".."])
        for itm in path_list:
            if itm == "":
                continue
            if itm in special_char_set:
                if itm == ".":
                    continue
                else:
                    if stck:
                        stck.pop()
            else:
                stck.append(itm)
                
        return "/"+"/".join(stck)