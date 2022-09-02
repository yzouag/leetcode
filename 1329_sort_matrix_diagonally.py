from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1 if i else n):
                rj = zip(mat[i:], range(j, n))
                vals = iter(sorted(r[j] for r, j in rj))
                for r, j in rj:
                    r[j] = next(vals)
        return mat

if __name__ == "__main__":
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    print(Solution().diagonalSort(mat))
    # assert [[1,1,1,1],[1,2,2,2],[1,2,3,3]] == Solution().diagonalSort(mat)

    # mat =  [[11,25,66,1,69,7],
    #         [23,55,17,45,15,52],
    #         [75,31,36,44,58,8],
    #         [22,27,33,25,68,4],
    #         [84,28,14,11,5,50]]
    # assert [[5,17,4,1,52,7],
    #         [11,11,25,45,8,69],
    #         [14,23,25,44,58,15],
    #         [22,27,31,36,50,66],
    #         [84,28,75,33,55,68]] == Solution().diagonalSort(mat)