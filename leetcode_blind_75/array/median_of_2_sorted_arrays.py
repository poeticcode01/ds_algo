from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n :
            return self.findMedianSortedArrays(nums2,nums1)

        low = 0
        high = m
        half_size = (m+n+1)//2
        INT_MIN = -(10**6+1)
        INT_MAX = 10**6+1
        while low <= high:
            slice1 = (low + high)//2
            slice2 = half_size - slice1

            slice1_left = INT_MIN if slice1 == 0 else nums1[slice1-1]
            slice2_left = INT_MIN if slice2 == 0 else nums2[slice2-1]

            slice1_right = INT_MAX if slice1 == m else nums1[slice1]
            slice2_right = INT_MAX if slice2 == n else nums2[slice2]

            if slice1_left <= slice2_right and slice2_left <=  slice1_right:
                if (m+n)%2 == 0:
                    return (max(slice1_left,slice2_left)+min(slice2_right,slice1_right))/2
                else:
                    return max(slice1_left,slice2_left)
            elif slice1_left > slice2_right:
                high = slice1 - 1
            else:
                low = slice1 + 1

            

if __name__ == "__main__":
    nums1 = [1,3]
    nums2 =[2]
    print(Solution().findMedianSortedArrays(nums1,nums2))