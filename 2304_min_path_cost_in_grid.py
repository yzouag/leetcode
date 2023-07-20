from typing import List

def minPathCost(grid: List[List[int]], moveCost: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    current_layer_cost = grid[-1][:]
    for i in range(1, m):
        new_current_layer_cost = [0] * n
        for j in range(n):
            node = grid[m-i-1][j]
            new_current_layer_cost[j] = node + min(moveCost[node][k] + current_layer_cost[k] for k in range(n))
        current_layer_cost = new_current_layer_cost
    return min(current_layer_cost)

grid = [[5,3],[4,0],[2,1]]
moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
print(minPathCost(grid, moveCost))
# Output: 17

grid = [[5,1,2],[4,0,3]]
moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]
print(minPathCost(grid, moveCost))
# Output: 6