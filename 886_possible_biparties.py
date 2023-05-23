from typing import List
from collections import defaultdict, deque
def possibleBipartition(n: int, dislikes: List[List[int]]) -> bool:
    adjacent_matrix = defaultdict(list)
    for a, b in dislikes:
        adjacent_matrix[a].append(b)
        adjacent_matrix[b].append(a)
    
    color = {}
    for i in range(1, n+1):
        if i in color:
            continue
        
        color[i] = 0
        queue = deque([i])
        while queue:
            node = queue.popleft()
            for neighbor in adjacent_matrix[node]:
                if neighbor in color:
                    if color[neighbor] == color[node]:
                        return False
                else:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
    
    return True

n = 4
dislikes = [[1,2],[1,3],[2,4]]
print(possibleBipartition(n, dislikes))
# Output: true

n = 3
dislikes = [[1,2],[1,3],[2,3]]
print(possibleBipartition(n, dislikes))
# Output: false