from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    # greedy approach
    # 1 2 3 2 1 2 4 5 1
    # we will find all local minimum and maximum
    # why? say for 1232, if we choose 2 instead of maxima 3, then we cannot include the last 2
    # so it is always better to choose the lowest and highest

    # special cases
    n = len(nums)
    if n < 2:
        return n
    
    prev_diff = nums[1] - nums[0]
    if prev_diff == 0:
        res = 1
    else:
        res = 2

    for i in range(2, n):
        curr_diff = nums[i] - nums[i-1]
        if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
            res += 1
            prev_diff = curr_diff
    return res

nums = [1, 7, 4, 9, 2, 5]
print(wiggleMaxLength(nums))
# Output: 6

nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(wiggleMaxLength(nums))
# Output: 7

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(wiggleMaxLength(nums))
# Output: 2
