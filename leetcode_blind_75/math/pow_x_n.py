class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        temp = abs(n)
        while temp > 0:
            if temp%2:
                # print(x)
                ans *= x
            x = x*x
            temp = temp//2
        # print(ans)
        if n < 0:
            return 1/ans
        return ans