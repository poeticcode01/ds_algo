class Solution:
    def reverseBits(self, n: int) -> int:
        bit_mask =0xFFFFFFFF
        n = n & bit_mask
        # ans = [0 for i in range(32)]
        i = 0
        ans = 0
        while n:
            rem = n % 2
            n = n//2
            ans = ans + (rem*(2**(31-i)))
            i +=1
        return ans