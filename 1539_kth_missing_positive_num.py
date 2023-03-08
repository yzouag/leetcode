from typing import List
def findKthPositive(arr: List[int], k: int) -> int:
    # method 1: O(n) time
    # counts = 0
    # prev = 0
    # for num in arr:
    #     gap = num - prev - 1
    #     if counts + gap >= k:
    #         return prev + k - counts
    #     else:
    #         counts += gap
    #     prev = num
    # return k - counts + prev

    # method 2: binary search
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] - mid - 1 < k: # more missing num requires
            l = mid + 1
        else:
            r = mid
    return r + k
    


arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))
# Output: 9

arr = [1,2,3,4]
k = 2
print(findKthPositive(arr, k))
# Output: 6