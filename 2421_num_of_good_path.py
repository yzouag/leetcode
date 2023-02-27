from typing import List
from collections import defaultdict

class Union_Find:
    def __init__(self, n: int, vals: List[int]) -> None:
        self.roots = [i for i in range(n)]
        self.sizes = [1] * n
        self.vals = vals

    def union(self, curr: int, node: int) -> None:
        root = self.find(node)
        curr_root = self.find(curr)
        if root == curr_root:
            return
        self.roots[root] = curr_root
        if self.vals[root] == self.vals[curr_root]:
            self.sizes[curr_root] += self.sizes[root]
        self.roots[node] = curr_root

    def find(self, node: int) -> int:
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]


def numberOfGoodPaths(vals: List[int], edges: List[List[int]]) -> int:
    adjacentList = defaultdict(list)
    for a, b in edges:
        adjacentList[a].append(b)
        adjacentList[b].append(a)
    nodesByValue = defaultdict(list)
    for i, val in enumerate(vals):
        nodesByValue[val].append(i)
    
    unionFind = Union_Find(len(vals), vals)
    res = len(vals)
    for k in sorted(nodesByValue):
        for node in nodesByValue[k]:
            for neighbor in adjacentList[node]:
                if vals[neighbor] <= vals[node]:
                    unionFind.union(node, neighbor)
        for node in nodesByValue[k]:
            if unionFind.find(node) == node:
                res += unionFind.sizes[node] * (unionFind.sizes[node]-1) // 2
    return res


# vals = [1,3,2,1,3]
# edges = [[0,1],[0,2],[2,3],[2,4]]
# print(numberOfGoodPaths(vals, edges))
# # Output: 6

# vals = [1,1,2,2,3]
# edges = [[0,1],[1,2],[2,3],[2,4]]
# print(numberOfGoodPaths(vals, edges))
# # Output: 7

# vals = [1]
# edges = []
# print(numberOfGoodPaths(vals, edges))
# # Output: 1

vals = [2,5,5,1,5,2,3,5,1,5]
edges = [[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]
print(numberOfGoodPaths(vals, edges))
# Output: 20
