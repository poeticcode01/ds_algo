class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        
        nums_len = len(nums)
        suff_max = [itm for itm in nums]
        i = nums_len - 2

        while i >= 0:
            suff_max[i] = max(suff_max[i],suff_max[i+1])
            i -=1

        i = 1
        min_so_far = nums[0]

        while i < nums_len - 1:
            if min_so_far < nums[i] and nums[i] < suff_max[i+1]:
                return True

            min_so_far = min(min_so_far,nums[i])
            i +=1

        return False