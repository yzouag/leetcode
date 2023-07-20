from typing import List
import heapq

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    heap = [(nums1[0]+nums2[0], 0, 0)]
    l1 = len(nums1)
    l2 = len(nums2)

    memo = set()
    
    res = []
    counts = 0
    while counts < k:
        if not heap:
            return res
        _, i1, i2 = heapq.heappop(heap)
        if (i1, i2) in memo:
            continue
        memo.add((i1, i2))
        res.append([nums1[i1], nums2[i2]])
        counts += 1
        if i1+1 < l1:
            heapq.heappush(heap, (nums1[i1+1]+nums2[i2], i1+1, i2))
        if i2+1 < l2:
            heapq.heappush(heap, (nums1[i1]+nums2[i2+1], i1, i2+1))
    return res

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(kSmallestPairs(nums1, nums2, k))
# Output: [[1,2],[1,4],[1,6]]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(kSmallestPairs(nums1, nums2, k))
# Output: [[1,1],[1,1]]

nums1 = [1,2]
nums2 = [3]
k = 3
print(kSmallestPairs(nums1, nums2, k))
# Output: [[1,3],[2,3]]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(kSmallestPairs(nums1, nums2, k))
# Output: [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]