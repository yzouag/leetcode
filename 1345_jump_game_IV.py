from typing import List
from collections import defaultdict
def minJumps(arr: List[int]) -> int:
    adj = defaultdict(list)
    for i,n in enumerate(arr):
        adj[n].append(i)
    N = len(arr)
    stack = [0]
    steps = 0
    visited = set()
    while stack:
        temp = []
        for node in stack:
            if node >= N or node < 0 or node in visited:
                continue
            if node == N-1:
                return steps
            visited.add(node)
            temp.append(node + 1)
            temp.append(node - 1)
            temp.extend(adj[arr[node]])
            adj.pop(arr[node]) # this step is important! remove redundant search!
        stack = temp
        steps += 1
    return -1


arr = [100,-23,-23,404,100,23,23,23,3,404]
print(minJumps(arr))
# Output: 3

arr = [7]
print(minJumps(arr))
# Output: 0

arr = [7,6,9,6,9,6,9,7]
print(minJumps(arr))
# Output: 1