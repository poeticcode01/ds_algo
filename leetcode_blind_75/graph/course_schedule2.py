from collections import defaultdict,deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = dict()
        course_graph = defaultdict(list)
        for course in range(numCourses):
            indegree[course] =0

        for course_prereq in prerequisites:
            indegree[course_prereq[0]] +=1
            course_graph[course_prereq[1]].append(course_prereq[0])

        zero_degree_set = set()
        for course, degree in indegree.items():
            if degree == 0:
                zero_degree_set.add(course)

        course_taken = []
        while len(zero_degree_set) > 0:
            # course_taken +=1
            cur_course = zero_degree_set.pop()
            course_taken.append(cur_course)
            for dependent_course in course_graph[cur_course]:
                indegree[dependent_course] -=1
                if indegree[dependent_course] == 0:
                    zero_degree_set.add(dependent_course)
        
        return course_taken if len(course_taken)==numCourses else []