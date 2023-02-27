from typing import List
def maximumTop(nums: List[int], k: int) -> int:
    if k == 0:
        return nums[0]
    if k < len(nums):
        return max(nums[:k-1])
    if k > len(nums):
        return max(nums)

nums = [5,2,2,4,0,6]
k = 4
print(maximumTop(nums, k))
# Output: 5

nums = [2]
k = 1
print(maximumTop(nums, k))
# Output: -1