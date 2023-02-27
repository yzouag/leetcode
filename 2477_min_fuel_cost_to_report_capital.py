import math
from typing import List
from collections import defaultdict
def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    if not roads:
        return 0
    if len(roads) == 1:
        return 1
    
    adjacentList = defaultdict(list)
    for road in roads:
        adjacentList[road[0]].append(road[1])
        adjacentList[road[1]].append(road[0])
    
    res = 0
    visited = set()

    def people_at_node(node: int) -> int:
        nonlocal res
        if len(adjacentList[node]) == 1 and adjacentList[node][0] in visited: # leaf node
            res += 1
            return 1
        visited.add(node)
        num = 1
        for neighbor in adjacentList[node]:
            if neighbor not in visited:
                num += people_at_node(neighbor)
        if node != 0:
            res += math.ceil(num/seats)
        return num
    
    people_at_node(0)
    return res

roads = [[0,1],[0,2],[0,3]]
seats = 5
print(minimumFuelCost(roads, seats))
# Output: 3

roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
print(minimumFuelCost(roads, seats))
# Output: 7

roads = []
seats = 1
print(minimumFuelCost(roads, seats))
# Output: 0