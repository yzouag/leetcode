from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    n = len(mat)

    total = 0
    for i in range(n):
        if i != n-i-1:
            total += mat[i][i]
        total += mat[i][n-i-1]
    return total

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(diagonalSum(mat))
# Output: 25

mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
print(diagonalSum(mat))
# Output: 8

mat = [[5]]
print(diagonalSum(mat))
# Output: 5