from typing import List
from math import ceil
def minEatingSpeed(piles: List[int], h: int) -> int:
    N = len(piles)
    if N > h:
        return -1
    if N == h:
        return max(piles)
    
    l, r = 1, max(piles)
    while l < r:
        mid = (l + r) // 2
        total_h = 0
        for pile in piles:
            total_h += ceil(pile/mid)
        if total_h > h:
            l = mid + 1
        else:
            r = mid
    return r

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))
# Output: 4

piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h))
# Output: 30

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))
# Output: 23