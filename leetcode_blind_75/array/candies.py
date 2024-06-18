from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for i in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        i = len(ratings) - 2
        while i >= 0:
            if ratings[i] >ratings[i+1]:
                temp = candies[i+1] + 1
                candies[i] = max(candies[i],temp)
            i -=1
        return sum(candies)