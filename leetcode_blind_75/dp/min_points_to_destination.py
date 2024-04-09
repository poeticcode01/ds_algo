class Solution:
    def minPoints(self, m, n, points):
        req = [[1]*n for i in range(m)]
        col = n-1
        if points[m-1][n-1] < 0:
            req[m-1][n-1] = 1 - points[m-1][n-1]

        for col in range(n-1,-1,-1):
            for  row in range(m-1,-1,-1):
                if row == m-1 and col == n -1:
                    continue
            rt =  None
            down = None
            if col + 1 < n:
                rt = req[row][col+1]
            if row + 1 < m:
                down = req[row+1][col]

            if rt and down:
                temp = min(rt,down)
                reqr = max(1,temp-points[row][col])
            elif not rt:
                reqr = max(1,down-points[row][col])
            else:
                reqr = max(1,rt-points[row][col])

            req[row][col] = reqr

        return req[0][0]