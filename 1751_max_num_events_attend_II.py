from typing import List
import bisect
def maxValue(events: List[List[int]], k: int) -> int:
    events.sort()
    n = len(events)
    
    memo = {}
    def dfs(i, curr_k):
        if i >= n or curr_k == k:
            return 0
        
        if (i, curr_k) in memo:
            return memo[(i, curr_k)]
        
        # 1. choose current event
        new_i = bisect.bisect_right(events, events[i][1], lo=i, key=lambda x: x[0])
        value1 = events[i][2] + dfs(new_i, curr_k+1)

        # 2. skip current event
        value2 = dfs(i+1, curr_k)

        memo[(i, curr_k)] = max(value1, value2)
        return memo[(i, curr_k)]
    
    return dfs(0, 0)
        

events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2
print(maxValue(events, k))
# Output: 7

events = [[1,2,4],[3,4,3],[2,3,10]]
k = 2
print(maxValue(events, k))
# Output: 10

events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
k = 3
print(maxValue(events, k))
# Output: 9