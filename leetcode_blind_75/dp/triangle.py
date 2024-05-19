from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row_cnt = len(triangle)
        nxt_row = []
        for i in range(row_cnt):
            temp = []
            for itm  in triangle[i]:
                temp.append(itm)
            nxt_row.append(temp)


        cur_row = row_cnt - 2

        while cur_row >= 0:
            for ind,itm in enumerate(triangle[cur_row]):
                # print(cur_row,nxt_row[cur_row][ind])
                nxt_row[cur_row][ind] = itm + min(nxt_row[cur_row+1][ind],nxt_row[cur_row+1][ind+1])
            cur_row -=1
        # print(nxt_row)
        return nxt_row[0][0]