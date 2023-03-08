from typing import List
import heapq

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    soldiers_heap = []
    for i in range(len(mat)):
        soldiers = 0
        for num in mat[i]:
            if num == 1:
                soldiers += 1
            else:
                break
        heapq.heappush(soldiers_heap, (soldiers, i))
    res = []
    for _ in range(k):
        _, index = heapq.heappop(soldiers_heap)
        res.append(index)
    return res

mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
print(kWeakestRows(mat, k))
# Output: [2,0,3]

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
print(kWeakestRows(mat, k))
# Output: [0,2]
