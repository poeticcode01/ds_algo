from collections import defaultdict,deque
import heapq
from typing import List
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        row = len(maze)
        col =  len(maze[0])
        
        temp = [1]*(col+2)
        new_maze = [temp]
        for cur_row in range(row):
            new_maze.append([1]+maze[cur_row]+[1])
        new_maze.append(temp)
        start[0] = start[0]+1
        start[1] = start[1] +1
        destination[0] = destination[0]+1
        destination[1] = destination[1] +1
       
        maze_graph = []
        for cur_row in range(row+2):
            temp = []
            for cur_col in range(col+2):
                temp.append([])
            maze_graph.append(temp)
        

        for cur_row in range(row+2):
            for cur_col in range(col+2):
                if new_maze[cur_row][cur_col] == 1:
                    temp_row = cur_row - 1 
                    while temp_row >= 0 and new_maze[temp_row][cur_col] != 1:
                        
                        maze_graph[temp_row][cur_col].append(((cur_row-1,cur_col),cur_row-temp_row-1))
                        temp_row -=1
                    temp_row = cur_row +1
                    while temp_row < row+2 and new_maze[temp_row][cur_col] != 1:
                        maze_graph[temp_row][cur_col].append(((cur_row+1,cur_col),temp_row-cur_row-1))
                        temp_row +=1
                    temp_col = cur_col + 1
                    while temp_col < col+2 and new_maze[cur_row][temp_col] != 1:
                        maze_graph[cur_row][temp_col].append(((cur_row,cur_col+1),temp_col-cur_col-1))
                        temp_col +=1
                    temp_col = cur_col - 1
                    while temp_col >= 0 and new_maze[cur_row][temp_col] != 1:
                        maze_graph[cur_row][temp_col].append(((cur_row,cur_col-1),cur_col-temp_col-1))
                        temp_col -=1

        
        visited = set()
        
        min_heap = [(0,(start[0],start[1]))]
        while min_heap:
            steps_count,cur_cell = heapq.heappop(min_heap)
            cell_row,cell_col = cur_cell
            if cell_row == destination[0] and cell_col == destination[1]:
                return steps_count
                
            if cur_cell in visited:
                continue
            visited.add(cur_cell)
            for frnd , dist in maze_graph[cell_row][cell_col]:
                heapq.heappush(min_heap,(dist+steps_count,frnd))        

        return -1