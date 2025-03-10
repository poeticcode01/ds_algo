from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for ind,itm in enumerate(timePoints):
            hh ,mm = itm.split(":")
            total_time = int(hh)*60+int(mm)
            timePoints[ind] = total_time
        
        timePoints = sorted(timePoints)
        min_diff = float('inf')
        ind = 1
        while ind < len(timePoints):
            min_diff = min(min_diff,timePoints[ind] - timePoints[ind-1])
            ind +=1

        min_diff = min(min_diff,1440+timePoints[0]-timePoints[-1])
        return min_diff