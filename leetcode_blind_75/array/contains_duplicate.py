from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_set = set()
        for itm in nums:
            if itm in element_set:
                return True
            element_set.add(itm)
        return False