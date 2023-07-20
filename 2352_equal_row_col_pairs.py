from typing import List
from collections import defaultdict

def equalPairs(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    row_hashes = defaultdict(int)
    for i in range(m):
        row_hashes[tuple(grid[i])] += 1

    res = 0
    for j in range(n):
        col = tuple(grid[i][j] for i in range(m))
        res += row_hashes[col]
    return res

grid = [[3,2,1],
        [1,7,6],
        [2,7,7]]
print(equalPairs(grid))
# Output: 1

grid = [[3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]]
print(equalPairs(grid))
# Output: 3