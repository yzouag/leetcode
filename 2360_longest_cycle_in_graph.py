from typing import List
from collections import defaultdict

def longestCycle(edges: List[int]) -> int:
    # visited = set()
    # res = -1
    # for node, next_node in enumerate(edges):
    #     if node in visited:
    #         continue
            
    #     visited.add(node)
        
    #     dist = {}
    #     distance = 0
    #     dist[node] = distance
    #     while next_node!= -1:
    #         if next_node not in visited:
    #             distance += 1
    #             dist[next_node] = distance
    #             visited.add(next_node)
    #             next_node = edges[next_node]
    #         else:
    #             if next_node in dist:
    #                 res = max(res, distance + 1 - dist[next_node])
    #             break
    # return res

    # topological sort
    indegrees = defaultdict(int)
    zero_indegrees = set(list(range(len(edges))))
    for node in edges:
        if node != -1:
            indegrees[node] += 1
            zero_indegrees.discard(node)
    
    visited = set()
    while zero_indegrees:
        node = zero_indegrees.pop()
        visited.add(node)
        if edges[node] != -1:
            indegrees[edges[node]] -= 1
            if indegrees[edges[node]] == 0:
                zero_indegrees.add(edges[node])
    
    res = -1
    for i in range(len(edges)):
        if i not in visited:
            cycle = 1
            node = edges[i]
            while node != i:
                visited.add(node)
                cycle += 1
                node = edges[node]
            res = max(res, cycle)

    return res
            


edges = [3,3,4,2,3]
print(longestCycle(edges))
# Output: 3

edges = [2,-1,3,1]
print(longestCycle(edges))
# Output: -1