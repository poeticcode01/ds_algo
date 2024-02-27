from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        ind = 1
        ans = 0
        prv = intervals[0]
        while ind < len(intervals):
            cur_interval = intervals[ind]
            if cur_interval[0] < prv[1]:
                if prv[1] > cur_interval[1]:
                    prv = cur_interval
                ans +=1
            else:
                prv = cur_interval
            ind +=1
                
        return ans