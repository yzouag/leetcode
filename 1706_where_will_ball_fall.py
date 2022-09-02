from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        height, width = len(grid), len(grid[0])
        res = []
        for i in range(width):
            current_level = 0
            current_pos = i
            while current_level < height:
                if grid[current_level][current_pos] == 1 and current_pos < width-1 and grid[current_level][current_pos+1] == 1:
                    current_pos += 1
                    current_level += 1
                elif grid[current_level][current_pos] == -1 and current_pos > 0 and grid[current_level][current_pos-1] == -1:
                    current_level += 1
                    current_pos -= 1
                else:
                    current_pos = -1
                    break
            res.append(current_pos)
        return res



if __name__ == "__main__":
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    assert [1,-1,-1,-1,-1] == Solution().findBall(grid)

    grid = [[-1]]
    assert [-1] == Solution().findBall(grid)

    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    assert [0,1,2,3,4,-1] == Solution().findBall(grid)