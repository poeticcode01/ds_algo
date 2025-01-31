from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)

        points = sorted(points)
        ref_sphere = points[0]
        
        ind = 1
        interval_count = 0
        
        while ind < len(points):
            cur_sphere = points[ind]
            max_end = ref_sphere[1]

            while ind < len(points) and cur_sphere[0] <= max_end:
                max_end = min(max_end,cur_sphere[1])
                ind +=1
                if ind < len(points):
                    cur_sphere = points[ind]
            if ind == len(points):
                interval_count +=1
                break
            else:
                interval_count +=1
                ref_sphere = points[ind]
    
        return interval_count