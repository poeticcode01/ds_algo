from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        # if len(intervals) == 1  :
        #     cur_interval = intervals[0]
        #     if cur_interval[0] < 
        #     ans.append([min(cur_interval[0],newInterval[0]),max(cur_interval[1],newInterval[1])])
        #     return ans
            
        ans = []
        ind = 0
        flag = False
        while ind  < len(intervals):
            cur_interval = intervals[ind]
            nxt = None
            if ind + 1 < len(intervals):
                nxt = intervals[ind+1]
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

            

            elif cur_interval[0] <= newInterval[0] and nxt and nxt[0] > newInterval[0]:
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
            elif not nxt and cur_interval[0] <= newInterval[0] and cur_interval[1] >= newInterval[0]:
                flag = True
                ans.append([min(cur_interval[0],newInterval[0]),max(cur_interval[1],newInterval[1])])
            
            else: 
                ans.append(cur_interval)
            ind +=1
        if not flag:
            ans.append(newInterval)
        return ans