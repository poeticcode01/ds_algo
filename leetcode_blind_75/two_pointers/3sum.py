from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        self.found = set()
        # print(nums)
        for ind,itm in enumerate(nums):
 
            low = ind + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] + nums[ind] == 0:
                
                    triplet = (nums[ind],nums[low],nums[high])
                    if triplet not in self.found:
                        ans.append(list(triplet))
                        self.found.add(triplet)

                    low +=1
                elif nums[low] + nums[high] + nums[ind] < 0:
                    low +=1
                else:
                    high -=1

        return ans