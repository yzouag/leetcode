from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    stones_inv = [-x for x in stones]
    heapq.heapify(stones_inv)
    while len(stones_inv) > 1:
        x = heapq.heappop(stones_inv)
        y = heapq.heappop(stones_inv)
        if x != y:
            heapq.heappush(stones_inv, x-y)
    return -stones_inv[0] if stones_inv else 0
    

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))
# Output: 1

stones = [1]
print(lastStoneWeight(stones))
# Output: 1