from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        visited = set()
        for x1,y1 in points:
            for x2,y2 in visited:
                if (x1,y2) in visited and (x2,y1) in visited:
                    size = abs(x2-x1)*abs(y2-y1)
                    min_area = min(size,min_area)
            visited.add((x1,y1))
        return min_area if min_area != float('inf') else 0