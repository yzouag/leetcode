from typing import List
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # how to get the O(1) space efficiency is the key to this question
    # we use first row and first column as the indicator
    # if matrix[i][j] == 0, set matrix[i][0], matrix[0][j] to 0
    # the problem is, in this case, if matrix[0][2] == 0, we will set matrix[0][0] to 0, which will zero out the first column
    # this is wrong, so we need an extra variable to indicate if first row or first column is 0 (this is a corner case)

    first_row_zero = False
    first_column_zero = False
    m, n = len(matrix), len(matrix[0])
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i == 0:
                    first_row_zero = True
                if j == 0:
                    first_column_zero = True
                if i != 0 and j != 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    if first_column_zero:
        for i in range(m):
            matrix[i][0] = 0
    
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0


matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
setZeroes(matrix)
print(matrix)
# Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
setZeroes(matrix)
print(matrix)
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]