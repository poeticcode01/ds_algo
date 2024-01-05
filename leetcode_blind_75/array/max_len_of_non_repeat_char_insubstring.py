class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s)
        if str_len  <= 1:
            return str_len 
        i = 0
        j = 1
        char_set = set()
        char_set.add(s[0])
        ans = 1
        while j < str_len:
            if s[j] in char_set:
                while len(char_set)!= 0 and (i < j) and s[i] != s[j]:
                    char_set.remove(s[i])
                    i+=1
                char_set.remove(s[i])
                char_set.add(s[j])
                i +=1
            else:
                char_set.add(s[j])
                ans = max(ans,j-i+1)
            j +=1
        return ans


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))