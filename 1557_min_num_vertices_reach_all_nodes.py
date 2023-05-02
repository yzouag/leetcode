from typing import List

def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    indegrees = [0] * n
    for _, to_node in edges:
        indegrees[to_node] += 1
    res = []
    for i, num in enumerate(indegrees):
        if num == 0:
            res.append(i)
    return res

n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(findSmallestSetOfVertices(n, edges))
# Output: [0,3]

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(findSmallestSetOfVertices(n, edges))
# Output: [0,2,3]