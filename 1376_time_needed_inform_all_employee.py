from typing import List
from collections import defaultdict
def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    directory_tree = defaultdict(list)
    for i, parent in enumerate(manager):
        if parent == -1:
            continue
        directory_tree[parent].append(i)

    def dfs(head):
        if head not in directory_tree:
            return 0
        return informTime[head] + max(dfs(sub) for sub in directory_tree[head])
    
    return dfs(headID)

n = 1
headID = 0
manager = [-1]
informTime = [0]
print(numOfMinutes(n, headID, manager, informTime))
# Output: 0

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
print(numOfMinutes(n, headID, manager, informTime))
# Output: 1