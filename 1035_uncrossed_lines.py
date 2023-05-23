from typing import List
def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    memo = {}
    m, n = len(nums1), len(nums2)
    def dfs(i: int, j: int) -> int:
        if i >= m or j >= n:
            return 0
        if (i, j) in memo:
            return memo[(i,j)]
        if nums1[i] == nums2[j]:
            memo[(i,j)] = 1 + dfs(i+1, j+1)
        else:
            memo[(i,j)] = max(dfs(i+1, j), dfs(i, j+1))
        return memo[(i,j)]
    return dfs(0,0)

nums1 = [1,4,2]
nums2 = [1,2,4]
print(maxUncrossedLines(nums1, nums2))
# Output: 2

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
print(maxUncrossedLines(nums1, nums2))
# Output: 3

nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]
print(maxUncrossedLines(nums1, nums2))
# Output: 2