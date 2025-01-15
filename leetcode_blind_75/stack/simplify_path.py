class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        simple_path = []
        stck = []
        special_char_set = set([".","..","..."])
        # print(path_list)
        for ind, itm in enumerate(path_list):
            if itm == "":
                continue

            if itm in special_char_set:
                if itm == ".":
                    continue
                elif itm == "..":
                    if stck:
                        stck.pop()
                else:
                    stck.append(itm)
            else:
                stck.append(itm)

        # print(stck)
        ans_str = "/".join(stck)
        ans_str = "/"+ans_str

        return ans_str