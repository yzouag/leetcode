from typing import List


def closedIsland(grid: List[List[int]]) -> int:
    visited = set()
    m, n = len(grid), len(grid[0])
    directions = [(0,-1), (-1, 0), (0,1), (1,0)]
    
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            if (i, j) in visited:
                continue
            
            # BFS
            queue = [(i, j)]
            visited.add((i, j))
            touchBoundary = False
            while queue:
                temp = []
                for x, y in queue:
                    if not touchBoundary:
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            touchBoundary = True
                    for direction in directions:
                        new_x = direction[0] + x
                        new_y = direction[1] + y
                        if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                            temp.append((new_x, new_y))
                            visited.add((new_x, new_y))
                queue = temp               
            if not touchBoundary:
                res += 1

    return res



grid = [[1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]
print(closedIsland(grid))
# Output: 2

grid = [[0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]]
print(closedIsland(grid))
# Output: 1

grid = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]
print(closedIsland(grid))
# Output: 2
