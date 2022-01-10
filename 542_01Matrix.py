from typing import List
import collections
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # method 1: BFS
        # q = collections.deque()
        # H, W = len(mat), len(mat[0])
        # for i in range(H):
        #     for j in range(W):
        #         if mat[i][j] == 0:
        #             q.append((i,j))
        #         else:
        #             mat[i][j] = -1

        # while q:
        #     i, j = q.popleft()
        #     if i > 0:
        #         if mat[i-1][j] == -1:
        #             mat[i-1][j] = mat[i][j] + 1
        #             q.append((i-1, j))
        #     if j > 0:
        #         if mat[i][j-1] == -1:
        #             mat[i][j-1] = mat[i][j] + 1
        #             q.append((i, j-1))
        #     if i < H - 1:
        #         if mat[i+1][j] == -1:
        #             mat[i+1][j] = mat[i][j] + 1
        #             q.append((i+1, j))
        #     if j < W - 1:
        #         if mat[i][j+1] == -1:
        #             mat[i][j+1] = mat[i][j] + 1
        #             q.append((i, j+1))
        # return mat

        # method 2: DP
        H, W = len(mat), len(mat[0])
        for i in range(H):
            for j in range(W):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i > 0 else math.inf
                    left = mat[i][j-1] if j > 0 else math.inf
                    mat[i][j] = min(top+1, left+1)
        
        for i in range(H-1, -1, -1):
            for j in range(W-1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i+1][j] if i < H-1 else math.inf
                    right = mat[i][j+1] if j < W-1 else math.inf
                    mat[i][j] = min(mat[i][j], bottom+1, right+1)
        return mat


if __name__ == "__main__":
    mat1 = [
        [0, 0, 0], 
        [0, 1, 0], 
        [0, 0, 0]
    ]

    mat2 = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    mat3 = [
        [0,1,0,1,1],
        [1,1,0,0,1],
        [0,0,0,1,0],
        [1,0,1,1,1],
        [1,0,0,0,1]
    ]

    assert [
        [0,0,0],
        [0,1,0],
        [0,0,0] 
    ] == Solution().updateMatrix(mat1)

    assert [
        [0,0,0],
        [0,1,0],
        [1,2,1]
    ] == Solution().updateMatrix(mat2)

    assert [
        [0,1,0,1,2],
        [1,1,0,0,1],
        [0,0,0,1,0],
        [1,0,1,1,1],
        [1,0,0,0,1]
    ] == Solution().updateMatrix(mat3)