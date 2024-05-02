from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq_dict = defaultdict(int)
        for cur_char in t:
            t_freq_dict[cur_char] +=1

        req = len(t_freq_dict.keys())
        cur = 0
        min_ans = None
        lft = None
        rt = None
        strt = 0
        end = 0
        run_freq = defaultdict(int)
        # print(req)
        while  end < len(s):
            run_freq[s[end]] +=1
            if  run_freq[s[end]] == t_freq_dict[s[end]]:
                cur +=1
   
                
            while cur == req:
                if not min_ans:
                    lft = strt
                    rt = end
                    min_ans = (end-strt+1)
                elif (end-strt+1) < min_ans:
                    min_ans = (end-strt+1)
                    lft = strt
                    rt = end
                run_freq[s[strt]] -=1
                if  run_freq[s[strt]] < t_freq_dict[s[strt]]:
                    cur -=1
                strt +=1
                    
            end +=1
        # print(min_ans)
        return s[lft:rt+1] if min_ans else ""