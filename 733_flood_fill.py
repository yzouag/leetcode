from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # method 1: depth first search
        # origin_color = image[sr][sc]
        # R, C = len(image), len(image[0])
        # def dfs(sr, sc):
        #     if image[sr][sc] == origin_color:
        #         image[sr][sc] = newColor
        #         if sr >= 1:
        #             dfs(sr-1, sc)
        #         if sc >= 1:
        #             dfs(sr, sc-1)
        #         if sr < R - 1:
        #             dfs(sr+1, sc)
        #         if sc < C -1:
        #             dfs(sr, sc+1)
        # dfs(sr, sc)

        # method 2 breadth first search
        q = deque([(sr, sc)])
        origin_color = image[sr][sc]
        R, C = len(image), len(image[0])
        if origin_color != newColor:
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                if i >= 1 and image[i-1][j] == origin_color: q.append((i-1, j))
                if j >= 1 and image[i][j-1] == origin_color: q.append((i, j-1))
                if i < R-1 and image[i+1][j] == origin_color: q.append((i+1, j))
                if j < C-1 and image[i][j+1] == origin_color: q.append((i, j+1))
        return image

if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    assert [[2,2,2],[2,2,0],[2,0,1]] == Solution().floodFill(image, sr, sc, newColor)
