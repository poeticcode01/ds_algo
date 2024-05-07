from collections import defaultdict
import copy
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_freq_dict = defaultdict(int)

        for word in words:
            word_freq_dict[word] +=1
        word_len =  len(words[0])  
        substring_len = len(words)*word_len
        strt = 0
        s_len = len(s)
        ans = []
        while strt + substring_len - 1 < s_len:
            temp_dict = copy.deepcopy(word_freq_dict)
           
            i = strt 
            count = 0
            while i + word_len <= strt + substring_len:
                temp_word =  s[i:i+word_len]
                if temp_dict[temp_word] >= 1:
                    count +=1
                    temp_dict[temp_word] -=1
                i += word_len
            if count == len(words):
                ans.append(strt)
            strt +=1
        return ans