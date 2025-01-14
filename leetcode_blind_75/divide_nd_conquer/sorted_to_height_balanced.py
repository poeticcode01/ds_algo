# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.mergeSort(nums)


    def mergeSort(self,nums):
        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return None

        n = len(nums)
        lft = self.mergeSort(nums[:n//2])
        rt = self.mergeSort(nums[n//2+1:])

        cur_node = TreeNode(nums[n//2])
        cur_node.left = lft
        cur_node.right = rt

        return cur_node