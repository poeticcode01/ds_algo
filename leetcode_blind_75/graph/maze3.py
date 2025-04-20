import heapq
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        row = len(maze)
        col =  len(maze[0])
        
        temp = [1]*(col+2)
        new_maze = [temp]
        for cur_row in range(row):
            new_maze.append([1]+maze[cur_row]+[1])
        new_maze.append(temp)

        ball[0] = ball[0]+1
        ball[1] = ball[1] +1

        hole[0] = hole[0]+1
        hole[1] = hole[1] +1
       
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
                        if temp_row == cur_row -1:
                            temp_row -=1
                            continue
                        maze_graph[temp_row][cur_col].append(((cur_row-1,cur_col),cur_row-temp_row-1,"d"))
                        temp_row -=1
                    temp_row = cur_row +1
                    while temp_row < row+2 and new_maze[temp_row][cur_col] != 1:
                        if temp_row == cur_row +1:
                            temp_row +=1
                            continue
                        maze_graph[temp_row][cur_col].append(((cur_row+1,cur_col),temp_row-cur_row-1,"u"))
                        temp_row +=1
                    temp_col = cur_col + 1
                    while temp_col < col+2 and new_maze[cur_row][temp_col] != 1:
                        if temp_col == cur_col +1:
                            temp_col +=1
                            continue
                        maze_graph[cur_row][temp_col].append(((cur_row,cur_col+1),temp_col-cur_col-1,"l"))
                        temp_col +=1
                    temp_col = cur_col - 1
                    while temp_col >= 0 and new_maze[cur_row][temp_col] != 1:
                        if temp_col == cur_col -1:
                            temp_col -=1
                            continue
                        maze_graph[cur_row][temp_col].append(((cur_row,cur_col-1),cur_col-temp_col-1,"r"))
                        temp_col -=1

        cur_row = hole[0] 
        cur_col = hole[1]
        temp_row = cur_row - 1 
        while temp_row >= 0 and new_maze[temp_row][cur_col] != 1:
            maze_graph[temp_row][cur_col].append(((cur_row,cur_col),cur_row-temp_row,"d"))
            temp_row -=1
        temp_row = cur_row +1
        while temp_row < row+2 and new_maze[temp_row][cur_col] != 1:
            maze_graph[temp_row][cur_col].append(((cur_row,cur_col),temp_row-cur_row,"u"))
            temp_row +=1
        temp_col = cur_col + 1
        while temp_col < col+2 and new_maze[cur_row][temp_col] != 1:
            maze_graph[cur_row][temp_col].append(((cur_row,cur_col),temp_col-cur_col,"l"))
            temp_col +=1
        temp_col = cur_col - 1
        while temp_col >= 0 and new_maze[cur_row][temp_col] != 1:
            maze_graph[cur_row][temp_col].append(((cur_row,cur_col),cur_col-temp_col,"r"))
            temp_col -=1

        
        visited = set()
        
        min_heap = [(0,(ball[0],ball[1]),"")]
        ans = []
        min_steps_count = float('inf')
        while min_heap:
            steps_count,cur_cell,path = heapq.heappop(min_heap)
            
            cell_row,cell_col = cur_cell
            if cell_row == hole[0] and cell_col == hole[1]:
                # print("hole",cell_row,cell_col)
                ans.append(path)
                # if steps_count < min_steps_count:
                #     print("found less min steps",steps_count,min_steps_count,path)
                min_steps_count = min(min_steps_count,steps_count)

            if steps_count > min_steps_count:
                break
                
            if cur_cell in visited:
                continue
            visited.add(cur_cell)
            # print(steps_count,cur_cell,path)
            for frnd , dist,dirn in maze_graph[cell_row][cell_col]:
                # print("friends",(dist+steps_count,frnd,path+dirn))
                heapq.heappush(min_heap,(dist+steps_count,frnd,path+dirn)) 
        # print(ans)
        if len(ans) == 0:
            return "impossible"
        return sorted(ans)[0]
        