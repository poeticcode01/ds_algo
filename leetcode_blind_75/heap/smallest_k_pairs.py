import heapq
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        cur_ind = 0
        max_heap = []
        ans = []
        while cur_ind < len(nums1):

            flag = False
            for itm in nums2:
                cur_pair_sum = nums1[cur_ind]+itm
                # print(len(max_heap))
                if len(max_heap) < k:
                    flag = True     
                    heapq.heappush(max_heap,(-cur_pair_sum,[nums1[cur_ind],itm]))
                else:     
                    if cur_pair_sum  < -max_heap[0][0]:
                        flag = True
                        temp = heapq.heappop(max_heap)
                        heapq.heappush(max_heap,(-cur_pair_sum,[nums1[cur_ind],itm]))
                    else:
                        break

            if not flag:
                break

            cur_ind +=1

        while max_heap:
            temp = heapq.heappop(max_heap)
            ans.append(temp[1])
        
        # print(ans)

        return list(reversed(ans))
    
if __name__ == "__main__":
    nums1 = [1,2,4,5,6]
    nums2 = [3,5,7,9]

    print(Solution().kSmallestPairs(nums1,nums2,3))