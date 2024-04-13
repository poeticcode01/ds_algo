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

            else:
                if cur_interval[0] > newInterval[1]:
                    ans.append(newInterval)
                    ans.extend(intervals[ind:])
                    break
                elif cur_interval[0] == newInterval[1] or cur_interval[1] >= newInterval[1]:
                    min_itm = min(newInterval[0],cur_interval[0])
                    ans.append([min_itm,cur_interval[1]])
                    ans.extend(intervals[ind+1:])
                    break
                else:
                    # print(ind,"h")
                    min_itm = min(newInterval[0],cur_interval[0])
                    while ind < len(intervals) and cur_interval[1] < newInterval[1]:
                        ind +=1
                        if ind < len(intervals):
                            cur_interval = intervals[ind]
                    # print(ind,"th")
                    if ind == len(intervals):
                        ans.append([min_itm,newInterval[1]])
                    else:
                        if newInterval[1] >= cur_interval[0]:
                            ans.append([min_itm,cur_interval[1]])
                            ans.extend(intervals[ind+1:])
                        else:
                            ans.append([min_itm,newInterval[1]])
                            ans.extend(intervals[ind:])
                    break
            ind +=1

        return ans