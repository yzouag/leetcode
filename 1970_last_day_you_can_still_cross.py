from typing import List
from collections import defaultdict

# first thought: using BFS/DFS to check each state, until cannot reach bottom
# improvement: using binary search, first check the middle stage, and then decide to go previous or after


# better solution:
# using union find? (Why? cross the land, meaning the land is still connected, our goal is to find the last connected state)
# or, inversely, we want find the first time the water is connected from left to right (completely block land from top to bottom)
# note that two water cells are connected when they are diagonally connected
# another trick, to check if any of left column water is connected to right, just use a pseudo-node and connect all left to that pseudo
# all right to another pseudo, then check these two pseudo nodes are connected

class UnionFind:
    def __init__(self, row, col) -> None:
        self.parents = {}
        self.rank = defaultdict(lambda: 1)
        self.left = 0
        self.right = 1
        for i in range(row):
            for j in range(col):
                self.parents[(i, j)] = (i, j)
        self.parents[self.left] = self.left
        self.parents[self.right] = self.right

        for i in range(row):
            self.parents[(i, 0)] = self.left
            self.parents[(i, col-1)] = self.right

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)
        if p1 == p2:
            return
        
        if self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2
            self.rank[p2] += 1
    
    def are_connected(self, node1, node2):
        return self.find(self.parents[node1]) == self.find(self.parents[node2])
        

def latestDayToCross(row: int, col: int, cells: List[List[int]]) -> int:
    union_find = UnionFind(row, col)
    grid = [[0] * col for _ in range(row)]

    directions = [(-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1), (0, 1), (0, -1)]
    for i, cell in enumerate(cells):
        x = cell[0] - 1
        y = cell[1] - 1
        grid[x][y] = 1
        for dir in directions:
            new_x = x + dir[0]
            new_y = y + dir[1]
            if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 1:
                union_find.union((x, y), (new_x, new_y))
        if union_find.are_connected(union_find.left, union_find.right):
            return i


        

row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]
print(latestDayToCross(row, col, cells))
# Output: 2

row = 2
col = 2
cells = [[1,1],[1,2],[2,1],[2,2]]
print(latestDayToCross(row, col, cells))
# Output: 1

row = 3
col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
print(latestDayToCross(row, col, cells))
# Output: 3