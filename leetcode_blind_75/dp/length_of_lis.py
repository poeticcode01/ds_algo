from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for itm in nums[1:]:
            if itm > lis[-1]:
                lis.append(itm)
            elif itm < lis[-1]:
                ind = self.find_index(lis,itm)
                lis[ind] = itm
        return len(lis)

    def find_index(self,lis,key):
        strt = 0
        end = len(lis) - 1
        while strt <= end:
            mid = strt + (end-strt)//2
            if lis[mid] < key:
                strt = mid + 1
            else:
                end = mid - 1
        return strt