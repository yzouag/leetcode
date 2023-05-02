from typing import List

class UnionFind:
    def __init__(self, n) -> None:
        self.group = {i: i for i in range(1,n+1)}
        self.rank = {i: 0 for i in range(1,n+1)}

    def find(self, node: int) -> int:      
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
        
    def join(self, node1: int, node2: int):
        u = self.find(node1)
        v = self.find(node2)
        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            self.group[v] = u
        elif self.rank[u] < self.rank[v]:
            self.group[u] = v
        else:
            self.group[u] = v
            self.rank[v] += 1

    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)
    
    def all_connected(self) -> bool:
        counts = 0
        for k, v in self.group.items():
            if k == v:
                counts += 1
        return counts == 1


def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    unions_a = UnionFind(n)
    unions_b = UnionFind(n)

    edges.sort(reverse=True)
    
    result = 0
    for type, n1, n2 in edges:
        if type == 3:
            if unions_a.are_connected(n1, n2) and unions_b.are_connected(n1, n2):
                result +=1
            else:
                unions_a.join(n1, n2)
                unions_b.join(n1, n2)
        elif type == 2:
            if unions_b.are_connected(n1, n2):
                result += 1
            else:
                unions_b.join(n1, n2)
        else:
            if unions_a.are_connected(n1, n2):
                result += 1
            else:
                unions_a.join(n1, n2)

    if unions_a.all_connected() and unions_b.all_connected():
        return result
    return -1

n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(maxNumEdgesToRemove(n, edges))
# Output: 2

n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
print(maxNumEdgesToRemove(n, edges))
# Output: 0

n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
print(maxNumEdgesToRemove(n, edges))
# Output: -1