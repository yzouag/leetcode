from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        l, r = 0, len(matrix)-1
        if target < matrix[0][0]:
            return False
        
        row_index = 0
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][0]:
                row_index = mid
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                return True

        # find col
        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row_index][mid]:
                l = mid + 1
            elif target < matrix[row_index][mid]:
                r = mid - 1
            else:
                return True
        return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 30
    assert Solution().searchMatrix(matrix, target) == True

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    assert Solution().searchMatrix(matrix, target) == False

    matrix = [[1,3]]
    target = 3
    assert Solution().searchMatrix(matrix, target) == True