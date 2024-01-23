class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for i in range(n+1)]
        ways[0] ,ways[1] = 1,1
        for i in range(2,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]