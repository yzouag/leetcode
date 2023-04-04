from math import inf
from typing import List
from collections import defaultdict
def minScore(n: int, roads: List[List[int]]) -> int:
    parent = list(range(n))
        
    def find(p): 
        """Return the root of p."""
        if p != parent[p]:
            parent[p] = find(parent[p])
        return parent[p]
    
    mp = defaultdict(lambda : inf)
    for u, v, dist in roads: 
        uu = find(u-1)
        vv = find(v-1)
        parent[uu] = vv
        mp[uu] = mp[vv] = min(mp[uu], mp[vv], dist)
    return mp[find(0)] if find(0) == find(n-1) else -1


n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
print(minScore(n, roads))
# Output: 5

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
print(minScore(n, roads))
# Output: 2