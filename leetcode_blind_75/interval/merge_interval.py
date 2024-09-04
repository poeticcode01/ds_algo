from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        strt = intervals[0][0]
        end = intervals[0][1]

        ans = []
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= end:
                end = max(end,intervals[i][1])
            else:
                ans.append([strt,end])
                strt = intervals[i][0]
                end = intervals[i][1]
            i +=1

        ans.append([strt,end])
        return ans