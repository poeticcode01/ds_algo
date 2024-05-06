from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        i = 0
        ans = 0
        freq_dict = defaultdict(int)
        j = 0
        while i < len(s):
            freq_dict[s[i]] +=1
            while freq_dict[s[i]] > 1:
                freq_dict[s[j]] -=1
                j +=1
            temp = i-j+1
            ans = max(ans,temp)
            i +=1
        return ans