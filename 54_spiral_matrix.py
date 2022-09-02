from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, left = 0, 0
        down, right = len(matrix)-1, len(matrix[0])-1

        res = []
        while up <= down and left <= right:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if (up <= down):
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if (left <= right):
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert Solution().spiralOrder(matrix) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
