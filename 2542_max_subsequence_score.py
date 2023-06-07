# looks like a DP problem, but actually using heap
# key part: sort the nums2, then find k largest from nums1[0:i]
# where min must be at least nums2[i-1]

from typing import List
import heapq
def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    sorted_nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
    heap = []
    sum1 = 0
    for i in range(k):
        sum1 += sorted_nums[i][0]
        heapq.heappush(heap, sorted_nums[i][0])
    res = sum1 * sorted_nums[k-1][1]
    for i in range(k, len(sorted_nums)):
        sum1 += sorted_nums[i][0]
        sum1 -= heapq.heappushpop(heap, sorted_nums[i][0])
        # what about the case when min is not sorted_nums[i][1]?
        # this means sorted_nums[i][0] is not the k largest among sorted_nums[:i][0]
        # but no worry, we have calculated it in previous iterations with a larger sorted_nums[i][1]
        # so this scenario won't matter
        res = max(res, sum1*sorted_nums[i][1])
    return res

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
print(maxScore(nums1, nums2, k))
# Output: 12

nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1
print(maxScore(nums1, nums2, k))
# Output: 30