from typing import List
from collections import defaultdict

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    queries_with_index = list(zip(queries, list(range(len(queries)))))
    queries_with_index.sort(key=lambda x: x[0][2])
    edgeList.sort(key=lambda x: x[2])

    joined_components = {i: i for i in range(n)}
    def find(i):
        if joined_components[i] != i:
            joined_components[i] = find(joined_components[i])
        return joined_components[i]
    
    result = [False] * len(queries)
    i = 0
    num_edges = len(edgeList)
    for query in queries_with_index:
        a, b, length = query[0]
        index = query[1]
        while i < num_edges and edgeList[i][2] < length:
            u, v = edgeList[i][0], edgeList[i][1]
            u = find(u)
            v = find(v)
            if u != v:
                joined_components[v] = u
            i += 1
        if find(a) == find(b):
            result[index] = True

    return result
        

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]
print(distanceLimitedPathsExist(n, edgeList, queries))
# Output: [false,true]

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]
print(distanceLimitedPathsExist(n, edgeList, queries))
# Output: [true,false]