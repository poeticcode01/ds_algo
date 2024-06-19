class Solution:
    def reverseWords(self, s: str) -> str:
        s_len = len(s)
        reversed_string = s[::-1]
        rev_string_list = reversed_string.split(" ")
        ans = []
        # print(rev_string_list)
        for word in rev_string_list:
            # print(word)
            if word == "":
                continue
            else:
                temp = word[::-1]
                ans.append(temp)
        return " ".join(ans)