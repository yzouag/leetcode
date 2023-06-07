from typing import List
def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # key idea:
    # using two bits to represent the board
    # first bit as next state, second bit as currrent state
    # initially, all nodes are 01 or 00
    # then we iterate to set the first bit to be 0 or 1 according to the second bit
    
    # this is not faster, just looks fancy
    neighbor = lambda i, j: sum(board[x][y] & 1 # get second bit
                                for x in (i-1, i, i+1)
                                for y in (j-1, j, j+1)
                                if 0 <= x < len(board) and 0 <= y < len(board[0])
                                )
    for i in range(len(board)):
        for j in range(len(board[0])):
            counts = neighbor(i, j)
            if board[i][j] == 0 and counts == 3:
                board[i][j] = 2
            if board[i][j] == 1 and (counts == 3 or counts == 4):
                board[i][j] = 3
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] >>= 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [[1,1],[1,0]]
print(gameOfLife(board))
# Output: [[1,1],[1,1]]