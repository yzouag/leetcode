from typing import List
def cherryPickup(grid: List[List[int]]) -> int:
    

grid = [[0,1,-1],[1,0,-1],[1,1,1]]
print(cherryPickup(grid))
# Output: 5

grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
print(cherryPickup(grid))
# Output: 0