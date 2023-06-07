from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjacent_list = [[] for _ in range(numCourses)]
    indegrees = [0] * numCourses
    for start, end in prerequisites:
        adjacent_list[start].append(end)
        indegrees[end] += 1
    zero_indegree = [i for i in range(numCourses) if indegrees[i] == 0]
    counts = 0
    
    while zero_indegree:
        course = zero_indegree.pop(0)
        counts += 1
        for post_course in adjacent_list[course]:
            indegrees[post_course] -= 1
            if indegrees[post_course] == 0:
                zero_indegree.append(post_course)
    
    return counts == numCourses

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites))
# Output: true

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))
# Output: false