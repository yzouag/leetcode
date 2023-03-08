from typing import List
from collections import defaultdict
def maxJumps(arr: List[int], d: int) -> int:
    jumps = defaultdict(int)
    result = 0
    
    def dfs(i: int) -> int:
        nonlocal result
        if i in jumps:
            return jumps[i]
        left = max(0, i-d)
        right = min(len(arr)-1, i+d)
        max_jumps = 0
        for k in range(i-1, left-1, -1):
            if arr[k] >= arr[i]:
                break
            max_jumps = max(max_jumps, dfs(k))
        for k in range(i+1, right+1):
            if arr[k] >= arr[i]:
                break
            max_jumps = max(max_jumps, dfs(k))
        max_jumps += 1
        jumps[i] = max_jumps
        result = max(result, max_jumps)
        return max_jumps

    for i in range(len(arr)):
        dfs(i)
    return result

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
print(maxJumps(arr,d))
# Output: 4

arr = [3,3,3,3,3]
d = 3
print(maxJumps(arr,d))
# Output: 1

arr = [7,6,5,4,3,2,1]
d = 1
print(maxJumps(arr,d))
# Output: 7