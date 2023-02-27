from typing import List
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: # start and goal cannot have obstacle
        return 0
    
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    res = [0] * (n+1)
    res[1] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                res[j+1] = 0
            else:
                res[j+1] = res[j] + res[j+1]
    return res[-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
# Output: 2

obstacleGrid = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
# Output: 1