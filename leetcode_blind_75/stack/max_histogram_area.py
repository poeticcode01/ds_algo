from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stck = []
        ind = 0
        max_area = 0
        n = len(heights)
        while ind < n:
            if not stck:
                stck.append(ind)
                ind +=1
                continue
            else:
                # print(stck[-1])
                if heights[ind] >= heights[stck[-1]]:
                    stck.append(ind)
                    ind +=1
                    continue
                else:
                    while stck and heights[stck[-1]] > heights[ind]:
                        k = stck.pop()
                        if stck:
                            temp = (ind-stck[-1]-1)*heights[k]
                            max_area = max(temp,max_area)
                        else:
                            temp = (ind)*heights[k]
                            max_area = max(temp,max_area)
                    stck.append(ind)
                    ind +=1

        while stck:
            k = stck.pop()
            if stck:
                temp = (n-stck[-1]-1)*heights[k]
                max_area = max(temp,max_area)
            else:
                temp = (n)*heights[k]
                max_area = max(temp,max_area)

        return max_area