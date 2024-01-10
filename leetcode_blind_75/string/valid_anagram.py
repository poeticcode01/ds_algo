from collections import defaultdict
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        s_freq_table = self.get_freq_table(s)
        t_freq_table = self.get_freq_table(t)

        is_same = self.compare(s_freq_table,t_freq_table)
        if not is_same:
            return False
        is_same = self.compare(t_freq_table,s_freq_table)
        return False if not is_same else True
        


    def get_freq_table(self,strng):
        freq_table = defaultdict(int)
        for ind,itm in enumerate(strng):
            freq_table[itm]+=1
        return freq_table

    def compare(self,orig,dupl):
        for key,val in orig.items():
            if val != dupl[key]:
                return False
        return True
        

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s,t))