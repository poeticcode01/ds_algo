from collections import defaultdict
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.ans = []
        self.digit_char_map = defaultdict(list)
        cur_char = "a"
        for num in range(2,10):
            self.digit_char_map[num].append(cur_char)
            self.digit_char_map[num].append(chr(ord(cur_char) + 1))
            self.digit_char_map[num].append(chr(ord(cur_char) + 2))
            if num == 7 or num == 9:
                self.digit_char_map[num].append(chr(ord(cur_char) + 3))
                cur_char = chr(ord(cur_char) + 4)
            else:
                cur_char = chr(ord(cur_char) + 3)

        self.permuatation("",digits)
        return self.ans




    def permuatation(self,run_str,cur_digits):
        # print("here", cur_digits)
        if cur_digits == "":
            if run_str != "":
                self.ans.append(run_str)
            return

        for cur_char in self.digit_char_map[int(cur_digits[0])]:
            self.permuatation(run_str+cur_char,cur_digits[1:])

        return