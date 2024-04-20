from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        run_freq = defaultdict(int)
        strt = 0
        end = 0 
        ans = 0

        while end < len(s):
            run_freq[s[end]] +=1
            if run_freq[s[end]] > 1:
                while strt < end and s[strt] != s[end]:
                    run_freq[s[strt]] -=1
                    strt +=1
                if strt != end:
                    strt +=1
                run_freq[s[end]] = 1

            ans = max(ans,end-strt+1)
            end +=1
        return ans