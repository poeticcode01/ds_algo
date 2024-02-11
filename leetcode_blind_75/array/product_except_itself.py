from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]]
        for itm in nums[1:]:
            temp = prefix_product[-1]*itm
            prefix_product.append(temp)
        suffix_product = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            temp = suffix_product[-1]*nums[i]
            suffix_product.append(temp)
        suffix_product = list(reversed(suffix_product))

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix_product[i+1])
            elif i == len(nums) - 1:
                ans.append(prefix_product[i-1])
            else:
                temp = prefix_product[i-1] * suffix_product[i+1]
                ans.append(temp)
        return ans