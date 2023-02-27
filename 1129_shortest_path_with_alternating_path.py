from collections import defaultdict
from typing import List
def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    adjacentList = defaultdict(list)
    RED = 0
    BLUE = 1
    for edge in redEdges:
        adjacentList[edge[0]].append((edge[1], RED))
    for edge in blueEdges:
        adjacentList[edge[0]].append((edge[1], BLUE))

    stack = [(0,-1)]
    step = 0
    visited = set()
    res = [-1] * n

    while stack:
        temp = []
        for node, prevColor in stack:
            if (node, prevColor) not in visited:
                res[node] = min(res[node], step) if res[node] != -1 else step
                visited.add((node, prevColor))
                for neighbor, edgeColor in adjacentList[node]:
                    if edgeColor != prevColor:
                        temp.append((neighbor, edgeColor))
        stack = temp
        step += 1

    return res


n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []
print(shortestAlternatingPaths(n, redEdges, blueEdges))
# Output: [0,1,-1]

n = 3
redEdges = [[0,1]]
blueEdges = [[2,1]]
print(shortestAlternatingPaths(n, redEdges, blueEdges))
# Output: [0,1,-1]