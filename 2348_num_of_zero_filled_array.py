from typing import List

def zeroFilledSubarray(nums: List[int]) -> int:
    sub_zero_count = 0
    res = 0
    for num in nums:
        if num == 0:
            sub_zero_count += 1
        else:
            res += sub_zero_count * (sub_zero_count+1) // 2
            sub_zero_count = 0
    res += sub_zero_count * (sub_zero_count+1) // 2
    return res

nums = [1,3,0,0,2,0,0,4]
print(zeroFilledSubarray(nums))
# Output: 6

nums = [0,0,0,2,0,0]
print(zeroFilledSubarray(nums))
# Output: 9

nums = [2,10,2019]
print(zeroFilledSubarray(nums))
# Output: 0