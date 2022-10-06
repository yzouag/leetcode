from typing import List
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # method 1: rotate along 4 corners
    # n = len(matrix)
    # for i in range(n//2):
    #     for j in range(i, n-i-1):
    #         tmp = matrix[i][j]
    #         matrix[i][j] = matrix[n-j-1][i]
    #         matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
    #         matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
    #         matrix[j][n-i-1] = tmp

    # method 2: rotate = transpose + reflect
    n = len(matrix)
    def transpose(matrix):
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    def reflect(matrix):
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1] , matrix[i][j]
    transpose(matrix)
    reflect(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)
# Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print(matrix)
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]