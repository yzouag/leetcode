import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # MY IMPLEMENTATION, WAY TOOOOO SLOW, exceeds time limit, breadth first search
        # Also, it is better not to modify the input data
        # q = collections.deque()
        # R, C = len(grid), len(grid[0])
        # max_area = 0
        # for i in range(R):
        #     for j in range(C):
        #         if grid[i][j] == 1:
        #             q.append((i, j))
        #             temp = 0
        #             while q:
        #                 sr, sc = q.popleft()
        #                 if grid[sr][sc] == 1:
        #                     grid[sr][sc] = 2
        #                     temp += 1
        #                 if sr >= 1 and grid[sr - 1][sc] == 1:
        #                     q.append((sr - 1, sc))
        #                 if sc >= 1 and grid[sr][sc - 1] == 1:
        #                     q.append((sr, sc - 1))
        #                 if sr < R - 1 and grid[sr + 1][sc] == 1:
        #                     q.append((sr + 1, sc))
        #                 if sc < C - 1 and grid[sr][sc + 1] == 1:
        #                     q.append((sr, sc + 1))
        #             if temp > max_area:
        #                 max_area = temp
        # return max_area
        R, C = len(grid), len(grid[0])
        seen = set()

        def dfs(sr, sc):
            if 0 <= sr < R and 0 <= sc < C and (sr, sc) not in seen and grid[sr][sc] == 1:
                seen.add((sr, sc))
                return 1 + dfs(sr+1, sc) + dfs(sr-1, sc) + dfs(sr, sc+1) + dfs(sr, sc-1)
            return 0

        area = 0
        for i in range(R):
            for j in range(C):
                temp = dfs(i, j)
                if temp > area:
                    area = temp
        return area


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert 6 == Solution().maxAreaOfIsland(grid)

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert 0 == Solution().maxAreaOfIsland(grid)

    grid = [
        [1, 1, 0, 0, 0], 
        [1, 1, 0, 0, 0], 
        [0, 0, 0, 1, 1], 
        [0, 0, 0, 1, 1]
    ]
    assert 4 == Solution().maxAreaOfIsland(grid)
