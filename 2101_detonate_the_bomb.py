from typing import List
from collections import defaultdict

def maximumDetonation(bombs: List[List[int]]) -> int:
    n = len(bombs)
    adjacentList = defaultdict(list)
    for i, bomb in enumerate(bombs):
        for j in range(n):
            if i == j:
                continue
            distance = (bomb[0]-bombs[j][0])**2 + (bomb[1]-bombs[j][1])**2
            if distance <= bomb[2]**2:
                adjacentList[i].append(j)

    def dfs(i, visited):
        if i in visited:
            return 0
        visited.add(i)
        return 1 + sum(dfs(neighbor, visited) for neighbor in adjacentList[i])
            
    counts = 0
    for i in range(n):
        visited = set()
        counts = max(counts, dfs(i, visited))
        if counts == n:
            return counts
    return counts


bombs = [[2,1,3],
         [6,1,4]]
print(maximumDetonation(bombs))
# Output: 2

bombs = [[1,1,5],
         [10,10,5]]
print(maximumDetonation(bombs))
# Output: 1

bombs = [[1,2,3],
         [2,3,1],
         [3,4,2],
         [4,5,3],
         [5,6,4]]
print(maximumDetonation(bombs))
# Output: 5