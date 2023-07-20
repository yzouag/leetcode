from typing import List
import bisect
def countNegatives(grid: List[List[int]]) -> int:
    res = 0
    m = len(grid)
    n = len(grid[0])
    index = n
    for i in range(m):
        index = bisect.bisect_right(grid[i], 0, key=lambda x: -x, hi=index)
        res += n-index
        if index == 0:
            res += (m-i-1)*n
            break
    return res

grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
print(countNegatives(grid))
# Output: 8

grid = [[3,2],[1,0]]
print(countNegatives(grid))
# Output: 0