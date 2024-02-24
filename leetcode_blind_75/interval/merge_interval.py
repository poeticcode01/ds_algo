from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ref_interval = intervals[0]
        ind = 1
        ans = []
        flag = False
        while ind < len(intervals):
            cur_interval = intervals[ind]
            max_end = ref_interval[1]
            while  ind < len(intervals) and cur_interval[0] <= max_end:
                max_end = max(cur_interval[1],max_end)
                ind +=1
                if ind < len(intervals):
                    cur_interval = intervals[ind]
            if ind == len(intervals):
                ans.append([ref_interval[0],max_end])
                return ans
            else:
                flag = True
                ans.append([ref_interval[0],max_end])
                ref_interval = intervals[ind]
            ind +1
        
        return ans if flag else intervals