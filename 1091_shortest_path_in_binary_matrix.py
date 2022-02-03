from typing import List

from importlib_metadata import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        if grid[0][0] or grid[height-1][width-1]:
            return -1
        q = collections.deque([(0,0,1)]) # x, y, dist
        visited = set()
        visited.add((0,0))
        directions = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]
        while q:
            x, y, dist = q.popleft()
            for direction in directions:
                x_, y_ = (x + direction[0], y + direction[1])
                if 0 <= x_ < height and 0 <= y_ < width and (x_, y_) not in visited and grid[x_][y_]==0:
                    if (x_, y_) == (height-1, width-1):
                        return dist + 1
                    q.append((x_, y_, dist + 1))
                    visited.add((x_, y_))
        return -1


if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    assert 2 == Solution().shortestPathBinaryMatrix(grid)

    grid = [[0,0,0],[1,1,0],[1,1,0]]
    assert 4 == Solution().shortestPathBinaryMatrix(grid)

    grid = [[1,0,0],[1,1,0],[1,1,0]]
    assert -1 == Solution().shortestPathBinaryMatrix(grid)
