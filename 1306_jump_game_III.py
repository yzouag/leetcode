from typing import List

def canReach(arr: List[int], start: int) -> bool:
    visited = set()
    stack = [start]
    while stack:
        temp = []
        for node in stack:
            if node >= len(arr) or node < 0  or node in visited:
                continue
            if arr[node] == 0:
                return True
            visited.add(node)
            temp.append(node + arr[node])
            temp.append(node - arr[node])
        stack = temp

    return False

arr = [4,2,3,0,3,1,2]
start = 5
print(canReach(arr, start))
# Output: true

arr = [4,2,3,0,3,1,2]
start = 0
print(canReach(arr, start))
# Output: true

arr = [3,0,2,1,2]
start = 2
print(canReach(arr, start))
# Output: false