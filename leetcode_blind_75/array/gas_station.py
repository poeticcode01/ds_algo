from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        strt = 0
        prev = 0
        cur = 0
        gas_len = len(gas)
        while strt < gas_len:
            # print(strt,cur)
            temp = prev + gas[cur] - cost[cur]
            if temp >= 0:
                if (cur + 1)%gas_len == strt:
                    return strt
                else:
                    prev = temp
                    cur = (cur + 1)%gas_len
            else:
                if cur+1 <= strt:
                    return -1 
                strt = cur + 1
                cur = cur + 1
                prev = 0
        return -1
    
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    Solution().canCompleteCircuit(gas,cost)