class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur_num = 0
        strt = 0
        max_len = 0
        max_and = 0
        for end , itm in enumerate(nums):
            if itm > cur_num or itm < cur_num:
                strt = end
                cur_num = itm
            
            if cur_num > max_and:
                max_and = cur_num
                max_len = 1
            elif cur_num == max_and:
                max_len = max(max_len,end-strt+1)

        return max_len