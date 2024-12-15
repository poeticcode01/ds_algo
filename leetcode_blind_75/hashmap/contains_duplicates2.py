from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_ind_map = dict()

        for ind, itm in enumerate(nums):
            
            if itm in num_ind_map:
                if ind-num_ind_map[itm] <= k:
                    return True

            num_ind_map[itm] = ind

        return False