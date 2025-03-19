class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        # Approach1
        # strt_ind = 0
        # ans = 0
        # num = 0
        # for ind,itm in enumerate(nums):
        #     while (num & itm)!= 0:
        #         num ^=nums[strt_ind]
        #         strt_ind +=1
        #     num |=itm

        #     ans = max(ans,ind-strt_ind+1)
        # return ans

        #Approach2
        bit_pos_map = {}  
        start = 0  
        max_length = 0  

        for end, num in enumerate(nums):
            # Check each bit position (0 to 31, assuming 32-bit integers)
            for bit in range(32):
                if (num >> bit) & 1:  # If this bit is set in 'num'
                    if bit in bit_pos_map and bit_pos_map[bit] >= start:
                        # Conflict! Move 'start' beyond the last occurrence
                        start = bit_pos_map[bit] + 1
                    bit_pos_map[bit] = end  # Update bit position

            # Update max length of valid subarray
            max_length = max(max_length, end - start + 1)

        return max_length