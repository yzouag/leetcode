from typing import List
def minReorder(n: int, connections: List[List[int]]) -> int:
    pass

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, connections))
# Output: 3

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
print(minReorder(n, connections))
# Output: 2

n = 3
connections = [[1,0],[2,0]]
print(minReorder(n, connections))
# Output: 0