from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # // if A[mid] > A[low] -- and A[mid] < A[high] ===> A[low]
        # // if A[mid] > A[low] and A[mid] > A[high] ==> search right
        # // if A[mid] < A[low]  == search left
        # if len(nums) == 2:
        #     return min(nums[0],nums[1])

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high-low)//2
            if (nums[mid] >= nums[low]) and (nums[mid] <= nums[high] ):
                return nums[low]
            elif (nums[mid] >= nums[low]) and (nums[mid] >= nums[high] ):
                low = mid+1
            else:
                high = mid