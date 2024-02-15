class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_mask = 0xFFFFFFFF
        while (b & bit_mask) > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return (a & bit_mask) if b > 0 else a
    
if __name__ == "__main__":
    Solution().getSum(-3,-5)