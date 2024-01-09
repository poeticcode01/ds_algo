from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq_table = defaultdict(int)
        for ind,itm in enumerate(t):
            t_freq_table[itm]+=1
        s_len = len(s)
        have , need = 0,len(t_freq_table)
        res ,reslen = [-1,-1],float("infinity")
        lft = 0
        s_freq_table = defaultdict(int)
        for rt,itm in enumerate(s):
            s_freq_table[itm] +=1
            if itm in t_freq_table and s_freq_table[itm] == t_freq_table[itm]:
                have +=1

            while have == need:
                if (rt-lft+1) < reslen:
                    res =[lft,rt]
                    reslen = rt-lft+1
                s_freq_table[s[lft]] -=1
                if s[lft] in t_freq_table and s_freq_table[s[lft]] < t_freq_table[s[lft]]:
                    have -=1
                lft +=1
        l,r = res
        # print(res,reslen)
        return  s[l:r+1] if reslen != float("infinity")  else ""
    
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s,t))