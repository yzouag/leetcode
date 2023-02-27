from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    res = grid[0].copy()
    for j in range(1, len(grid[0])):
        res[j] = res[j-1] + res[j]

    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if j == 0:
                res[j] = res[j] + grid[i][j]
            else:
                res[j] = min(res[j-1] + grid[i][j], res[j] + grid[i][j])
    return res[-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
# Output: 7

grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))
# Output: 12