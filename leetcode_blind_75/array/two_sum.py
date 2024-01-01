from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = []
        for ind,itm in enumerate(nums):
            index_nums.append((itm,ind))

        sorted_nums = sorted(index_nums,key = lambda x: x[0])
        length = len(sorted_nums)
        for ind,itm in enumerate(sorted_nums):
            lookup_element = target - itm[0]
            search_list = sorted_nums[:ind] + sorted_nums[ind+1:]
            search_ind = self.binary_search(lookup_element,search_list)
            if search_ind == -1:
                continue
            else:
                return [itm[1],search_ind]

    def binary_search(self,key,search_list):
        low = 0
        high = len(search_list) - 1
        while low <= high:
            mid = low + (high-low)//2
            if search_list[mid][0] == key:
                 return search_list[mid][1]
            elif search_list[mid][0] < key:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target))