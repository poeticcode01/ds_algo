from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_tuple = [(''.join(sorted(itm)),itm) for itm in strs]
        str_tuple.sort(key=lambda x:x[0])
        ans = []
        ind =0
        while ind < len(str_tuple):
            j = ind +1
            temp = [str_tuple[ind][1]]
            ref = str_tuple[ind][0]
            while j < len(str_tuple) and str_tuple[j][0] == ref:
                temp.append(str_tuple[j][1])
                j +=1
            ans.append(temp)
            ind = j
        return ans
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))