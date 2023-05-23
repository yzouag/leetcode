from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1_copy = nums1[:m]
    i, j = 0, 0
    while i < m and j < n:
        if nums1_copy[i] < nums2[j]:
            nums1[i+j] = nums1_copy[i]
            i += 1
        else:
            nums1[i+j] = nums2[j]
            j += 1
    for i in range(i, m):
        nums1[i+j] = nums1_copy[i]
    for j in range(j, n):
        nums1[i+j] = nums2[j]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
# Output: [1,2,2,3,5,6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)
# Output: [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)
# Output: [1]