from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # height, width = len(board), len(board[0])
        # visited = set()
        # def dfs(x, y):
        #     board[x][y] = 'OO'
        #     visited.add((x, y))
        #     directions = [(1,0), (-1,0), (0,-1), (0,1)]
        #     for dir in directions:
        #         x_, y_ = x + dir[0], y + dir[1]
        #         if 0 <= x_ < height and 0 <= y_ < width and (x_, y_) not in visited and board[x_][y_] == 'O':
        #             dfs(x_, y_)
        
        # for i in range(height):
        #     if board[i][0] == "O" and (i, 0) not in visited:
        #         dfs(i, 0)
        #     if board[i][width-1] == 'O' and (i, width-1) not in visited:
        #         dfs(i, width-1)

        # for i in range(width):
        #     if board[0][i] == "O" and (0, i) not in visited:
        #         dfs(0, i)
        #     if board[height-1][i] == 'O' and (height-1, i) not in visited:
        #         dfs(height-1, i)

        # for i in range(height):
        #     for j in range(width):
        #         if board[i][j] == 'OO':
        #             board[i][j] = 'O'
        #         elif board[i][j] == 'O':
        #             board[i][j] = 'X'
        if not board or not board[0]:
            return
        def dfs(i, j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = '.'
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i-1, j)
                dfs(i+1, j)
        
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                dfs(i, j)
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(board)
    assert board == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    board = [["X"]]
    Solution().solve(board)
    assert board == [["X"]]