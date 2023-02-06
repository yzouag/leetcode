from typing import List, Set

def exist(board: List[List[str]], word: str) -> bool:
    m, n, l = len(board), len(board[0]), len(word)
    def dfs(i: int, j: int, w: int, visited: Set[tuple]):
        if (i, j) in visited:
            return False
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if board[i][j] == word[w] and w == l-1:
            return True
        if board[i][j] != word[w]:
            return False
        
        visited.add((i,j))
        adj = [[0,1], [0,-1], [1,0], [-1,0]]
        for x,y in adj:
            if dfs(i+x, j+y, w+1, visited):
                return True
        visited.remove((i,j))
        return False        
    
    w_ = set(word)
    b_ = set()
    for i in range(m):
        for j in range(n):
            b_.add(board[i][j])
    if not w_.issubset(b_):
        return False

    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0, set()): return True
    
    return False
        


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word)) # True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word)) # True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word)) # False

board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAAAAB"
print(exist(board, word)) # False