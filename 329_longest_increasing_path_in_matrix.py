from typing import List
def longestIncreasingPath(matrix: List[List[int]]) -> int:
    dp = {}
    m, n = len(matrix), len(matrix[0])

    def dfs(i, j, prev):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if matrix[i][j] <= prev:
            return 0
        if (i, j) in dp:
            return dp[(i,j)]
        dp[(i,j)] = 1 + max(dfs(ii, jj, matrix[i][j]) for (ii, jj) in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)])
        return dp[(i,j)]

    longest = 0
    for i in range(m):
        for j in range(n):
            longest = max(longest, dfs(i, j, float('-inf')))
    return longest

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
# Output: 4

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))
# Output: 4

matrix = [[1]]
print(longestIncreasingPath(matrix))
# Output: 1