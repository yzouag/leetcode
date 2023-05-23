from typing import List
from itertools import product

def shortestBridge(grid: List[List[int]]) -> int:
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    n = len(grid)

    island = []
    visited = set()

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= n:
            return
        if (i, j) in visited:
            return
        visited.add((i,j))
        if grid[i][j] == 0:
            island.append((i,j))
            return
        for dir in directions:
            dfs(dir[0]+i, dir[1]+j)

    for i, j in product(range(n), range(n)):
        if grid[i][j] == 1:
            dfs(i, j)
            break
    
    step = 1
    while True:
        temp = []
        for i,j in island:
            for dir in directions:
                new_i, new_j = dir[0]+i, dir[1]+j
                if (new_i, new_j) in visited or new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
                    continue
                if grid[new_i][new_j] == 1:
                    return step
                temp.append((new_i, new_j))
                visited.add((new_i, new_j))
        island = temp
        step += 1

                

grid = [[0,1],
        [1,0]]
print(shortestBridge(grid))
# Output: 1

grid = [[0,1,0],
        [0,0,0],
        [0,0,1]]
print(shortestBridge(grid))
# Output: 2

grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
print(shortestBridge(grid))
# Output: 1