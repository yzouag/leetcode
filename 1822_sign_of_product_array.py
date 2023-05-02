from typing import List
def arraySign(nums: List[int]) -> int:
    sign = 0
    for num in nums:
        if num > 0:
            continue
        elif num < 0:
            sign += 1
        else:
            return 0
    return 1 if sign % 2 == 0 else -1

nums = [-1,-2,-3,-4,3,2,1]
print(arraySign(nums))
# Output: 1

nums = [1,5,0,2,-3]
print(arraySign(nums))
# Output: 0

nums = [-1,1,-1,1,-1]
print(arraySign(nums))
# Output: -1