from typing import List, Set
def isBipartite(graph: List[List[int]]) -> bool:
    # set1 = set()
    # set2 = set()
    # visited = set()

    # def dfs(node: int, set1: Set[int], set2: Set[int], visited: Set[int]) -> bool:
    #     if node in visited:
    #         return True
    #     visited.add(node)
    #     set1.add(node)
    #     for neighbor in graph[node]:
    #         if neighbor in set1:
    #             return False
    #         if not dfs(neighbor, set2, set1, visited):
    #             return False
    #     return True

    # for i in range(len(graph)):
    #     if i in visited:
    #         continue
    #     if not dfs(i, set1, set2, visited):
    #         return False
    # return True

    color = {}
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor in color:
                if color[neighbor] == color[node]:
                    return False
            else:
                color[neighbor] = 1 - color[node]
                if not dfs(neighbor):
                    return False
        return True
    for i in range(len(graph)):
        if i not in color:
            color[i] = 0
            if not dfs(i):
                return False
    return True

graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(isBipartite(graph))
# Output: false

graph = [[1,3],[0,2],[1,3],[0,2]]
print(isBipartite(graph))
# Output: true