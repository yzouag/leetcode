from typing import List
from collections import defaultdict

def minReorder(n: int, connections: List[List[int]]) -> int:
    adjacent_matrix = defaultdict(list)

    for fromCity, toCity in connections:
        adjacent_matrix[fromCity].append((toCity, True))
        adjacent_matrix[toCity].append((fromCity, False))

    res = 0
    visited = set()
    def dfs(node):
        nonlocal res
        visited.add(node)
        for neighbor, existPath in adjacent_matrix[node]:
            if neighbor in visited:
                continue
            if existPath:
                res += 1
            dfs(neighbor)
    
    dfs(0)
    return res


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, connections))
# Output: 3

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
print(minReorder(n, connections))
# Output: 2

n = 3
connections = [[1,0],[2,0]]
print(minReorder(n, connections))
# Output: 0