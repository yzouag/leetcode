from typing import List
from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # # method 1
        # # pop indegree == 0
        # # create the adjacent list to store the neighbor relations
        # adj_list = defaultdict(list)
        # # the index of this array means the course index
        # indegree = [0]*numCourses
        # for prereq_pair in prerequisites:
        #     dest, source = prereq_pair[0], prereq_pair[1]
        #     adj_list[source].append(dest)
        #     indegree[dest] += 1
        # # scan the indegree list to get all nodes that have 0 indegree
        # zero_indegree_stack = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        # result = []
        # while zero_indegree_stack:
        #     node = zero_indegree_stack.popleft()
        #     result.append(node)
        #     # get all nodes the current node points to
        #     # decrease the indegree of these nodes
        #     # if the indegree of some nodes change to 0, update them into the zero indegree stack
        #     for neighbor in adj_list[node]:
        #         indegree[neighbor] -= 1
        #         if indegree[neighbor] == 0:
        #             zero_indegree_stack.appendleft(neighbor)
        # return result if len(result) == numCourses else []
        
        # method 2
        # dfs
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses
        for dest, source in prerequisites:
            adj_list[source].append(dest)
            indegrees[dest] += 1
        topological_order_list = []
        def dfs(node: int) -> None:
            topological_order_list.append(node)
            # change this node indegree to -1 to avoid second visit
            indegrees[node] -= 1
            for neighbor in adj_list[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    dfs(neighbor)
        for i in range(numCourses):
            if indegrees[i] == 0:
                dfs(i)
        return topological_order_list if len(topological_order_list) == numCourses else []

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    assert [0,1] == Solution().findOrder(numCourses, prerequisites)
        
