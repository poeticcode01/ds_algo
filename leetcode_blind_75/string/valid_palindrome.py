class Solution:
    def isPalindrome(self, s: str) -> bool:
        run_str = ""
        for char in s:
            if char.isalnum():
                run_str += char.lower()
        i = 0
        j = len(run_str) - 1
        while i < j:
            if run_str[i] != run_str[j]:
                return False
            i +=1
            j -=1
        return True