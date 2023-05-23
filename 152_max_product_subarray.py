from typing import List
def maxProduct(nums: List[int]) -> int:
    # product will be large, if positive * positive
    # or if it is a negative number, times the smallest negative number of previous subarray
    res = nums[0]
    imin, imax = res, res
    for i in range(1, len(nums)):
        if nums[i] < 0:
            imax, imin = imin, imax # if this number < 0, then current max will become next min, current min will be next max
        imax = max(nums[i], nums[i]*imax)
        imin = min(nums[i], nums[i]*imin)
        res = max(res, imax)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))
# Output: 6

nums = [-2,0,-1]
print(maxProduct(nums))
# Output: 0

nums = [-2,3,-4]
print(maxProduct(nums))
# Output: 24