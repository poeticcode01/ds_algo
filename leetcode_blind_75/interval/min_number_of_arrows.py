from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        ref_sphere = points[0]
        
        ans = []
        ind = 1
        flag = False
        # print(points)
        while ind < len(points):
            cur_sphere = points[ind]
            max_end = ref_sphere[1]
            while ind < len(points) and cur_sphere[0] <= max_end:
                max_end = min(max_end,cur_sphere[1])
                ind +=1
                if ind < len(points):
                    cur_sphere = points[ind]
            if ind == len(points):
                flag = True
                ans.append([ref_sphere[0],max_end])
                break
            else:
                flag = True
                ans.append([ref_sphere[0],max_end])
                ref_sphere = points[ind]

        return len(ans) if flag else len(points)