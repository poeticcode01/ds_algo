class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        str1_len = len(text1)
        str2_len = len(text2)
        lcs = [[0]*(str1_len+1) for i in range(str2_len+1)]
        ans = 0
        
        for i in range(1,str2_len+1):
            for j in range(1,str1_len+1):
               
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
                if text2[i-1] == text1[j-1]:
                    lcs[i][j] = max(lcs[i][j],lcs[i-1][j-1]+1)
                ans = max(ans, lcs[i][j])
        return ans