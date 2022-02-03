from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # edges cases:
        if not graph:
            return []
        
        # apply DFS on DAG
        stack = [(0, [0])]
        res = []
        while stack:
            node, path = stack.pop()
            # end point
            if node == len(graph) - 1:
                res.append(path)
            # traverse rest
            for nei in graph[node]:
                stack.append((nei, path+[nei]))
        return res

if __name__ == "__main__":
    graph = [[1,2],[3],[3],[]]
    print(Solution().allPathsSourceTarget(graph)) # output: [[0,1,3],[0,2,3]]

    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(Solution().allPathsSourceTarget(graph)) # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]