from typing import List
def maxSubArray(nums: List[int]) -> int:
    res = 0
    maximum = float('-inf')
    for num in nums:
        if res < 0:
            res = num
        else:
            res = res + num
        maximum = max(maximum, res)
    return maximum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
# Output: 6

nums = [1]
print(maxSubArray(nums))
# Output: 1

nums = [5,4,-1,7,8]
print(maxSubArray(nums))
# Output: 23