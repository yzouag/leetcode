from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    # pay attention to how to init 2d matrix in python
    matrix = [[0]*n for _ in range(n)]
    # method 1: use four for loops
    # left, up = 0, 0
    # right, bottom = n-1, n-1
    # num = 1
    # while left <= right and up <= bottom:
    #     for i in range(left, right+1):
    #         matrix[up][i] = num
    #         num += 1
    #     up += 1
    #     for i in range(up, bottom+1):
    #         matrix[i][right] = num
    #         num += 1
    #     right -= 1
    #     for i in range(right, left-1, -1):
    #         matrix[bottom][i] = num
    #         num += 1
    #     bottom -= 1
    #     for i in range(bottom, up-1, -1):
    #         matrix[i][left] = num
    #         num += 1
    #     left += 1
    # return matrix

    # method 2: use four directions
    row, column = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num = 1
    d = 0
    while num <= n*n:
        matrix[row][column] = num
        num += 1
        
        r = (row + directions[d][0]) % n
        c = (column + directions[d][1]) % n
        if matrix[r][c] != 0:
            d = (d + 1) % 4
        row += directions[d][0]
        column += directions[d][1]
    return matrix

n = 3
print(generateMatrix(n))
# Output: [[1,2,3],[8,9,4],[7,6,5]]

n = 1
print(generateMatrix(n))
# Output: [[1]]
