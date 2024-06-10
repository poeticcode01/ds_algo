from collections import defaultdict
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        freq_dict = defaultdict(int)


        for ind,itm in enumerate(nums):
            freq_dict[itm] +=1

        i = 0
        cur_ptr = 0
        while i < len(nums):
            max_fill = min(2,freq_dict[nums[i]])
            for j in range(max_fill):
                nums[cur_ptr+j] = nums[i]
            cur_ptr += max_fill
            i += freq_dict[nums[i]]
            
        return cur_ptr