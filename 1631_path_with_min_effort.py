from typing import List
from collections import defaultdict
import heapq

def minimumEffortPath(heights: List[List[int]]) -> int:
    # dijkstra algorithm
    dist = defaultdict(lambda: float('inf'))
    dist[(0, 0)] = 0
    boundary = [(0, 0, 0)]

    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    while boundary:
        d, r, c = heapq.heappop(boundary)
        for dir in directions:
            nr = r + dir[0]
            nc = c + dir[1]
            if nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]):
                nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                if nd < dist[(nr, nc)]:
                    dist[(nr, nc)] = nd
                    heapq.heappush(boundary, (nd, nr, nc))

    return dist[(len(heights)-1, len(heights[0])-1)]


heights = [[1, 2, 2], 
           [3, 8, 2], 
           [5, 3, 5]]
print(minimumEffortPath(heights))
# Output: 2

heights = [[1, 2, 3], 
           [3, 8, 4], 
           [5, 3, 5]]
print(minimumEffortPath(heights))
# Output: 1

heights = [[1, 2, 1, 1, 1], 
           [1, 2, 1, 2, 1], 
           [1, 2, 1, 2, 1], 
           [1, 2, 1, 2, 1], 
           [1, 1, 1, 2, 1]]
print(minimumEffortPath(heights))
# Output: 0
