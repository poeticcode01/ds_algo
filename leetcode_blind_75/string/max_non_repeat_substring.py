from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        j = 0
        str_len = len(s)
        freq_table = defaultdict(int)
        ans = 1
        while j < str_len:
        
            freq_table[s[j]] +=1
            if self.is_replacable(freq_table,k):
                ans = max(ans,j-i+1)
            else:
                while i < j and not self.is_replacable(freq_table,k):
                    freq_table[s[i]] -=1
                    i +=1
            j +=1
        return ans


    def is_replacable(self,freq_table,k):
        max_freq = -1
        freq_sum = 0
        for char,freq in freq_table.items():
            if freq > max_freq:
                max_freq = freq
            freq_sum += freq

        replacable_count = freq_sum - max_freq
        if replacable_count <= k:
            return True
        else:
            return False
        

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s,k))