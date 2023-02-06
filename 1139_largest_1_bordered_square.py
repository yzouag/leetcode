from typing import List

def largest1BorderedSquare(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

grid = [[1,1,1],[1,0,1],[1,1,1]]
print(largest1BorderedSquare(grid))
# Output: 9

grid = [[1,1,0,0]]
print(largest1BorderedSquare(grid))
# Output: 1