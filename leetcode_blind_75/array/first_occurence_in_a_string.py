from collections import deque
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        first_char_pos_list = []
        first_char = needle[0]
        dq = deque([])
        i = 0
        while i < len(haystack):
            if haystack[i] == first_char:
                dq.append(i)
            
            i +=1
            while dq:
                k = dq.popleft()
                if haystack[k:k+needle_len] == needle:
                    return k
        return -1