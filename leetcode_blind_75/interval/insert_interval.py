from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        ans = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                if newInterval[1] <  intervals[i][0]:
                    return ans + [newInterval] + intervals[i:]
                else:
                    strt = min(newInterval[0],intervals[i][0])
                    end = max(newInterval[1],intervals[i][1])
                    j = i+1
                    while j < len(intervals) and intervals[j][0] <= end:
                        end = max(end,intervals[j][1])
                        j +=1
                    return ans + [[strt,end]] + intervals[j:]
            i +=1