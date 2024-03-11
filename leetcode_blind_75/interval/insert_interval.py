from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            ans = [newInterval]+intervals
            return ans
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals


        ans = []
        ind = 0
        flag = False
        while ind  < len(intervals):
            cur_interval = intervals[ind]
            if  cur_interval[1] < newInterval[0]:
                ans.append(cur_interval)

            elif not flag and cur_interval[0] > newInterval[0]:
                flag = True
                min_itm = newInterval[0]
                while ind  < len(intervals) and newInterval[1] > intervals[ind][1]:
                    ind +=1
                if ind == len(intervals):
                    ans.append(newInterval)
                else:
                    if newInterval[1] >= intervals[ind][0]:
                        ans.append([min_itm,intervals[ind][1]])
                    else:
                        ans.append([min_itm,newInterval[1]])
                        ans.append(intervals[ind])

            elif cur_interval[0] <= newInterval[0] and  cur_interval[1] >= newInterval[0]:
                flag = True
                if newInterval[1] < cur_interval[1]:
                    ans.append(cur_interval)
                else:
                    
                    min_itm = min(cur_interval[0],newInterval[0])
                    ind +=1
                    while ind  < len(intervals) and newInterval[1] > intervals[ind][1]:
                        ind +=1
                    if ind == len(intervals):
                        ans.append([min_itm,newInterval[1]])
                    else:
                        if newInterval[1] >= intervals[ind][0]:
                            ans.append([min_itm,intervals[ind][1]])
                        else:
                            ans.append([min_itm,newInterval[1]])
                            ans.append(intervals[ind])
            else: 
                ans.append(cur_interval)
            ind +=1

        return ans