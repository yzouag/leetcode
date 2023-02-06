from collections import defaultdict
from typing import List

def minTime(n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    adjacent_matrix = defaultdict(list)
    for edge in edges:
        adjacent_matrix[edge[0]].append(edge[1])
        adjacent_matrix[edge[1]].append(edge[0])
    
    visited = set()
    valid_path = set()
    
    def dfs(node: int) -> bool:
        valid_point = hasApple[node]
        visited.add(node)
        for neighbor in adjacent_matrix[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    valid_point = True
                    valid_path.add((node, neighbor))
        return valid_point
    
    dfs(0)
    return 2 * len(valid_path)


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
print(minTime(n, edges, hasApple)) # 8

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]
print(minTime(n, edges, hasApple)) # 6

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,False,False,False,False,False]
print(minTime(n, edges, hasApple)) # 0

n = 2
edges = [[0,1]]
hasApple = [True, True]
print(minTime(n, edges, hasApple)) # 2

n = 7
edges = [[0,1],[0,2],[2,3],[1,4],[4,5],[4,6]]
hasApple = [False,False,True,False,False,False,False]
print(minTime(n, edges, hasApple)) # 2
