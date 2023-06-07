from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    def check_unit_valid(elements: List[str]) -> bool:
        counted = set()
        for ele in elements:
            if ele == '.':
                continue
            if ele in counted:
                return False
            counted.add(ele)
        return True

    # check horizontal
    for i in range(9):
        if not check_unit_valid(board[i]):
            return False

    # check vertical
    for i in range(9):
        if not check_unit_valid([board[j][i] for j in range(9)]):
            return False
    
    # check grid
    for i in range(3):
        for j in range(3):
            grid = []
            for k in range(3):
                grid.extend(board[i*3+k][j*3:j*3+3])
            if not check_unit_valid(grid):
                return False

    return True

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))
# Output: true

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))
# Output: false
