from typing import List
from collections import defaultdict

def countPairs(n: int, edges: List[List[int]]) -> int:
    adjacent_list = defaultdict(list)
    for a, b in edges:
        adjacent_list[a].append(b)
        adjacent_list[b].append(a)

    res = 0
    visited = set()

    for i in range(n):
        if i in visited:
            continue
        
        visited.add(i)
        queue = [i]
        num_nodes = 1
        while queue:
            temp = []
            for node in queue:
                for neighbor in adjacent_list[node]:
                    if neighbor not in visited:
                        temp.append(neighbor)
                        visited.add(neighbor)
                        num_nodes += 1
            queue = temp
        res += num_nodes * (n-num_nodes)
    
    return res//2

n = 3
edges = [[0,1],[0,2],[1,2]]
print(countPairs(n, edges))
# Output: 0

n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
print(countPairs(n, edges))
# Output: 14