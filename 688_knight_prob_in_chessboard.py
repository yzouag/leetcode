from copy import deepcopy
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    if k == 0:
        return 1
    
    prev_dp = [[1] * n for _ in range(n)]
    curr_dp = [[0] * n for _ in range(n)]
    
    directions = [(1,2), (-1,2), (-1,-2), (1,-2),
                  (2,1), (-2,1), (-2,-1), (2, -1)]
    for _ in range(k):
        for i in range(n):
            for j in range(n):
                curr_dp[i][j] = 0
                for dx, dy in directions:
                    if i - dx < 0 or i - dx >= n or j - dy < 0 or j - dy >= n:
                        continue
                    curr_dp[i][j] += prev_dp[i-dx][j-dy]
        prev_dp = deepcopy(curr_dp)

    return prev_dp[row][column]/(8**k)

n = 3
k = 2
row = 0
column = 0
print(knightProbability(n, k, row, column))
# Output: 0.06250

n = 1
k = 0
row = 0
column = 0
print(knightProbability(n, k, row, column))
# Output: 1.00000