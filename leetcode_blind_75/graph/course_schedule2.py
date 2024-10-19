from collections import defaultdict,deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        course_graph = defaultdict(list)
        indegree = defaultdict(int)
        all_course_set = set()
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        for _, courses in enumerate(prerequisites):

            course_graph[courses[1]].append(courses[0])
            indegree[courses[0]] +=1

            all_course_set.add(courses[0])
            all_course_set.add(courses[1])


        dq = deque([])
        for cur_course in range(numCourses):
            if indegree[cur_course] == 0:
                dq.append(cur_course)

        ordered_courses = []
        while dq:
            k = dq.popleft()
            ordered_courses.append(k)

            for frnd in course_graph[k]:
                indegree[frnd] -=1
                if indegree[frnd] == 0:
                    dq.append(frnd)

        if len(ordered_courses) == numCourses:
            return ordered_courses

        return []