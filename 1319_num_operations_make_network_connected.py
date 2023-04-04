from typing import List

def makeConnected(n: int, connections: List[List[int]]) -> int:
    if n > len(connections) + 1:
        return -1
    
    parents = list(range(n))

    def find(p):
        if parents[p] != p:
            parents[p] = find(parents[p])
        return parents[p]
    
    for u, v in connections:
        uu = find(u)
        vv = find(v)
        parents[uu] = vv

    brokenParts = 0
    for i, parent in enumerate(parents):
        if parent == i:
            brokenParts += 1

    return brokenParts-1


n = 4
connections = [[0,1],[0,2],[1,2]]
print(makeConnected(n, connections))
# Output: 1

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(makeConnected(n, connections))
# Output: 2

n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]
print(makeConnected(n, connections))
# Output: -1

n = 11
connections = [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]
print(makeConnected(n, connections))
# Output: 3
