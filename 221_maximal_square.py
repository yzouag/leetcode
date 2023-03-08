from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    # brute force
    # max_square = 0
    # m, n = len(matrix), len(matrix[0])
    # def expand(i, j):
    #     size = 1
    #     diagonal = (i, j)
    #     while True:
    #         if diagonal[0] + 1 >= m or diagonal[1] + 1 >= n or matrix[diagonal[0]+1][diagonal[1]+1] == '0':
    #             return size
    #         diagonal = (diagonal[0]+1, diagonal[1]+1)
    #         for x in range(i, diagonal[0]):
    #             if matrix[x][diagonal[1]] == '0':
    #                 return size
    #         for y in range(j, diagonal[1]):
    #             if matrix[diagonal[0]][y] == '0':
    #                 return size
    #         size += 1

    # for i in range(m):
    #     for j in range(n):
    #         if matrix[i][j] == '0':
    #             continue
    #         max_square = max(max_square, expand(i,j))
    # return max_square**2

    # dynamic programming
    # let dp[i,j] be the maximum square with bottom right corner at (i,j)
    # recurssive relationship:
    # dp[i+1,j+1] = min(dp[i,j], dp[i,j+1], dp[i+1, j]) + 1
    # explanation: form a new, larger square by put upper, left and diagonal square together
    dp = [0] + [int(i) for i in matrix[0]]
    max_square = max(dp)
    for i in range(1, len(matrix)):
        prev = 0
        for j in range(1, len(dp)):
            temp = dp[j] # temporarily store the prev
            if matrix[i][j-1] == '0':
                dp[j] = 0
            else:
                dp[j] = min([dp[j-1], dp[j], prev]) + 1 # dp[j] is the min of old dp[j] (or dp[i-1][j]), dp[j-1], old dp[j-1] or dp[i-1][j-1]
                max_square = max(dp[j], max_square)
            prev = temp # prev is the old dp[j-1]
    return max_square ** 2


matrix = [["1", "0", "1", "0", "0"], 
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], 
          ["1", "0", "0", "1", "0"]]
print(maximalSquare(matrix))
# Output: 4

matrix = [["0","1"],
          ["1","0"]]
print(maximalSquare(matrix))
# Output: 1

matrix = [["0"]]
print(maximalSquare(matrix))
# Output: 0