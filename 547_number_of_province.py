from typing import List

from importlib_metadata import collections


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # method 1: BFS
        # count = 0
        # numCircles = len(isConnected)
        # visited = set()
        # for i in range(numCircles):
        #     if i not in visited:
        #         count += 1
        #         q = collections.deque([i])
        #         while q:
        #             circle = q.popleft()
        #             for j in range(numCircles):
        #                 if isConnected[circle][j] == 1 and j not in visited:
        #                     visited.add(j)
        #                     q.append(j)
        # return count

        # method 2: DFS
        count = 0
        numCircles = len(isConnected)
        
        def dfs(i: int) -> None:
            for j in range(numCircles):
                if j not in visited and isConnected[i][j]:
                    visited.add(j)
                    dfs(j)
        
        visited = set()
        for i in range(numCircles):
            if i not in visited:
                count += 1
                dfs(i)
        return count


if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    assert 2 == Solution().findCircleNum(isConnected)

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    assert 3 == Solution().findCircleNum(isConnected)