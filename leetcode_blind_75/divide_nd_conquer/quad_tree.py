
# Definition for a QuadTree node.
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.dfs(len(grid),0,0)


    def dfs(self,n,r,c):
        allSame = True
        for i in range(n):
            for j in range(n):
                if self.grid[r][c] != self.grid[r+i][c+j]:
                    allSame = False
                    break

        if allSame:
            return Node(self.grid[r][c],True)

        n = n//2
        topleft = self.dfs(n,r,c)
        topright = self.dfs(n,r,c+n)
        bottomleft = self.dfs(n,r+n,c)
        bottomright = self.dfs(n,r+n,c+n)

        return Node(0,False,topleft,topright,bottomleft,bottomright)