from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for itm in s:
            s_freq[itm] +=1

        for itm in t:
            t_freq[itm] +=1

        
        i = 1
        while i < len(s):
            if (s[i] == s[i-1] and t[i] == t[i-1]) or  (s[i] != s[i-1] and t[i] != t[i-1]):
                if s_freq[s[i]] == t_freq[t[i]]:
                    i +=1
                else:
                    return False
            else:
                return False
        return True