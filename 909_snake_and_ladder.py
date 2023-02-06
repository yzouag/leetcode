from typing import List
from collections import defaultdict

def snakesAndLadders(board: List[List[int]]) -> int:
    n = len(board)
    # build adjacent matrix
    adjacent_matrix = defaultdict(list)
    for i in range(n*n):
        for j in range(1, 7):
            if i + j >= n*n: 
                break
            row = n-1 - (i+j)//n
            col = (i+j)%n if ((i+j)//n) % 2 == 0 else n-1-(i+j)%n
            if board[row][col] == -1:
                adjacent_matrix[i].append(i+j)
            else:
                adjacent_matrix[i].append(board[row][col]-1)

    # bfs
    step = 0
    stack = [0]
    visited = set()
    while stack:
        temp = []
        for node in stack:
            if node == n*n-1:
                return step
            if node not in visited:
                temp.extend(adjacent_matrix[node])
            visited.add(node)
        stack = temp
        step += 1

    return -1
        

    

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board)) # 4

board = [[-1,-1],[-1,3]]
print(snakesAndLadders(board)) # 1