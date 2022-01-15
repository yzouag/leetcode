from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        for i in range(1, len(triangle)):
            cur = triangle[i]
            for j in range(len(cur)):
                if j == 0 :
                    cur[j] = prev[0] + cur[j]
                elif j == len(cur) - 1:
                    cur[j] = prev[-1] + cur[j]
                else:
                    cur[j] = min(prev[j-1], prev[j]) + cur[j]
            prev = cur
        return min(prev)


if __name__ == "__main__":
    triangle1 = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert Solution().minimumTotal(triangle1)==11

    triangle2 = [[-10]]
    assert Solution().minimumTotal(triangle2) == -10