from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]
        cur_pow = 2
        if n > 0: 
            ans[1] = 1
        if n > 1:
            ans[2] = 1
        i = 3
        pow_ind = 2
        nxt_pow = 4
        prv_pow = 2
        while i < (n+1):
            if i == nxt_pow:
                pow_ind +=1
                prv_pow = nxt_pow
                nxt_pow = 2**pow_ind
                ans[i] = 1
                i +=1
                continue
            else:
                ans[i] = ans[prv_pow] + ans[(i-prv_pow)]
                i +=1
                continue
        return ans