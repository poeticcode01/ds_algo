from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2,nums1)

        low = 0
        high = n
        mid_size = (n+m+1)//2
        INT_MIN = -1000001
        INT_MAX = 1000001

        while low <=  high:
            cut1 = low + (high-low)//2
            cut2 = mid_size - cut1

            cut1_lft = INT_MIN if cut1 <= 0 else nums1[cut1-1]
            cut2_lft = INT_MIN if cut2 <= 0 else nums2[cut2-1]

            cut1_right = INT_MAX if cut1 >= n else nums1[cut1]
            cut2_right = INT_MAX if cut2 >= m else nums2[cut2]

            if cut1_lft <= cut2_right and cut2_lft <= cut1_right:
                if (n+m)%2 == 0:
                    return (max(cut1_lft,cut2_lft) + min(cut1_right,cut2_right))/2
                else:
                    return max(cut1_lft,cut2_lft)
            elif cut1_lft > cut2_right:
                high = cut1 -1
            else:
                low = cut1 + 1