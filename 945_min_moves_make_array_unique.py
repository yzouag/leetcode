from typing import List
def minIncrementForUnique(nums: List[int]) -> int:
    toAdd = 0
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            toAdd += nums[i-1] - nums[i] + 1
            nums[i] = nums[i-1] + 1
    return toAdd

nums = [1,2,2]
print(minIncrementForUnique(nums))
# Output: 1

nums = [3,2,1,2,1,7]
print(minIncrementForUnique(nums))
# Output: 6