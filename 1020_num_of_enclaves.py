from typing import List

def numEnclaves(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    visited = set()
    res = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            if (i, j) in visited:
                continue

            touchBoundary = False
            num_cells = 0

            queue = [(i, j)]
            visited.add((i,j))

            while queue:
                temp = []
                for node in queue:
                    num_cells += 1
                    if not touchBoundary and (node[0] == 0 or node[0] == m-1 or node[1] == 0 or node[1] == n-1):
                        touchBoundary = True
                    for dir in directions:
                        x = node[0] + dir[0]
                        y = node[1] + dir[1]
                        if (x, y) in visited:
                            continue
                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue
                        if grid[x][y] == 0:
                            continue
                        temp.append((x, y))
                        visited.add((x, y))
                queue = temp
            if not touchBoundary:
                res += num_cells

    return res

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(numEnclaves(grid))
# Output: 3

grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(numEnclaves(grid))
# Output: 0