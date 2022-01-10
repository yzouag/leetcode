from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # MY IMPLEMENTATION: SLOOOOOOOOW!!!
        # q = collections.deque()
        # H, W = len(grid), len(grid[0])
        # for i in range(H):
        #     for j in range(W):
        #         if grid[i][j] == 2:
        #             grid[i][j] = 0
        #             q.append((i,j))
        #         elif grid[i][j] == 1:
        #             grid[i][j] = -1
        # while q:
        #     i, j = q.popleft()
        #     if i > 0:
        #         if grid[i-1][j] == -1:
        #             grid[i-1][j] = grid[i][j] + 1
        #             q.append((i-1, j))
        #     if j > 0:
        #         if grid[i][j-1] == -1:
        #             grid[i][j-1] = grid[i][j] + 1
        #             q.append((i, j-1))
        #     if i < H - 1:
        #         if grid[i+1][j] == -1:
        #             grid[i+1][j] = grid[i][j] + 1
        #             q.append((i+1, j))
        #     if j < W - 1:
        #         if grid[i][j+1] == -1:
        #             grid[i][j+1] = grid[i][j] + 1
        #             q.append((i, j+1))
        # minutes = 0
        # for i in range(H):
        #     for j in range(W):
        #         if grid[i][j] > minutes:
        #             minutes = grid[i][j]
        #         if grid[i][j] == -1:
        #             return -1
        # return minutes

        rotten = collections.deque()
        H, W = len(grid), len(grid[0])
        fresh_cnt = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        minutes_passed = 0

        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    xx = dx+x
                    yy = dy+y
                    if 0 <= xx < H and 0 <= yy < W and grid[xx][yy] == 1:
                        fresh_cnt -= 1
                        grid[xx][yy] = 2
                        rotten.append((xx, yy))
        return minutes_passed if fresh_cnt == 0 else -1

if __name__ == "__main__":
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    grid2 = [[2,0,1],[0,1,0],[0,1,1]]
    grid3 = [[0,2]]

    assert Solution().orangesRotting(grid1) == 4
    assert Solution().orangesRotting(grid2) == -1
    assert Solution().orangesRotting(grid3) == 0
