class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for cur_char in s:
            if cur_char.isalnum():
                new_str +=cur_char
        
        new_str = new_str.lower()
        i = 0
        j = len(new_str) - 1
        # print(new_str)
        while i < j:
            if new_str[i] != new_str[j]:
                return False
            i +=1
            j -=1
        return True