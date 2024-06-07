from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_pos = 0
        i = 0
        j = 0
        temp = [0 for i in range(m+n)]

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp[merge_pos] = nums1[i]
                merge_pos +=1
                i +=1
            else:
                temp[merge_pos] = nums2[j]
                merge_pos +=1
                j +=1

        while i < m:
            temp[merge_pos] = nums1[i]
            merge_pos +=1
            i +=1

        while j < n:
            temp[merge_pos] = nums2[j]
            merge_pos +=1
            j +=1

        for i in range(m+n):
            nums1[i] = temp[i]