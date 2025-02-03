from typing import List


class Solution:
    def getPrefixMax(self,prices):

        min_so_far = prices[0]
        price_len = len(prices)

        pref_max = [0 for i in range(price_len)]
    
        for i in range(1,price_len):
            if prices[i] >= min_so_far:
                cur_profit = prices[i] - min_so_far
                self.max_profit = max(self.max_profit,cur_profit)
                pref_max[i]= max(pref_max[i-1],cur_profit)
            else:
                pref_max[i] = pref_max[i-1]
            
            min_so_far = min(min_so_far,prices[i])
                  

        return pref_max

    def getSuffixMax(self,prices):
        price_len = len(prices)
        max_so_far = prices[-1]
        
        suff_max = [0 for i in range(price_len)]

        i = price_len - 2
        while i >= 0:
            if prices[i] <= max_so_far:
                cur_profit = max_so_far - prices[i]
                self.max_profit = max(self.max_profit,cur_profit)
                suff_max[i]= max(suff_max[i+1],cur_profit)
            else:
                suff_max[i] = suff_max[i+1]


            max_so_far = max(max_so_far,prices[i])
            
            i -=1
        return suff_max

    def getMaxProfit(self,prices,pref_max,suff_max):
        price_len = len(prices)
        for i in range(1,price_len-1):
            self.max_profit = max(self.max_profit,pref_max[i]+suff_max[i+1])



    def maxProfit(self, prices: List[int]) -> int:
        self.max_profit = 0
        
        pref_max = self.getPrefixMax(prices)  
        suff_max = self.getSuffixMax(prices)

        self.getMaxProfit(prices,pref_max,suff_max)
        
        return self.max_profit