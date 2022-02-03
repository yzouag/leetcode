import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        count = 0
        seen = set()
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i, j) not in seen:
                    count += 1
                    q = collections.deque([(i,j)])
                    while q:
                        x, y = q.popleft()
                        if x > 0 and grid[x-1][y] == '1' and (x-1, y) not in seen:
                            seen.add((x-1,y))
                            q.append((x-1,y))
                        if y > 0 and grid[x][y-1] == '1'and (x, y-1) not in seen:
                            seen.add((x, y-1))
                            q.append((x,y-1))
                        if x < height - 1 and grid[x+1][y] == '1'and (x+1, y) not in seen:
                            seen.add((x+1, y))
                            q.append((x+1,y))
                        if y < width -1 and grid[x][y+1] == '1'and (x, y+1) not in seen:
                            seen.add((x, y+1))
                            q.append((x,y+1))
        return count

    
if __name__ == "__main__":   
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert 1 == Solution().numIslands(grid)

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert 3 == Solution().numIslands(grid)