from typing import List
from collections import defaultdict

# let dp[n][c] be the max frequency of color c for node n
# using topological order to ensure when we check node n,
# all its parent nodes have checked
def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    dp = [[0] * 26 for _ in range(n)]

    indegrees = defaultdict(int)
    adjacentList = defaultdict(list)
    for edge in edges:
        adjacentList[edge[0]].append(edge[1])
        indegrees[edge[1]] += 1
    
    zero_indegree = []
    for i in range(n):
        if indegrees[i] == 0:
            zero_indegree.append(i)

    nodes_visited = 0
    result = 0
    while zero_indegree:
        node = zero_indegree.pop()
        nodes_visited += 1
        dp[node][ord(colors[node])-ord('a')] += 1
        result = max(max(dp[node]), result)
        for neighbor in adjacentList[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                zero_indegree.append(neighbor)
            for i, freq in enumerate(dp[node]):
                if freq > dp[neighbor][i]:
                    dp[neighbor][i] = freq

    if nodes_visited < n:
        return -1
    
    return result


colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
print(largestPathValue(colors, edges))
# Output: 3

colors = "a"
edges = [[0,0]]
print(largestPathValue(colors, edges))
# Output: -1