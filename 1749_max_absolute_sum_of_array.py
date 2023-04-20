from typing import List
def maxAbsoluteSum(nums: List[int]) -> int:
    max_value = 0
    res = 0
    for num in nums:
        if num > 0:
            max_value = max(-res, max_value)
            if res + num > 0:
                res = 0
                continue
        res += num
    max_value = max(-res, max_value)

    res = 0
    for num in nums:
        if num < 0:
            max_value = max(res, max_value)
            if res + num < 0:
                res = 0
                continue
        res += num
    max_value = max(res, max_value)
    return max_value

nums = [1,-3,2,3,-4]
print(maxAbsoluteSum(nums))
# Output: 5

nums = [2,-5,1,-4,3,-2]
print(maxAbsoluteSum(nums))
# Output: 8