from typing import List


def minSubarray(nums: List[int], p: int) -> int:
    total_sum = sum(nums) % p
    if total_sum == 0:
        return 0
    remainders = {}
    prefix_sum = 0
    ret = float('inf')
    for i in range(len(nums)):
        prefix_sum = (nums[i] + prefix_sum) % p
        pair = (prefix_sum-total_sum) % p
        if pair in remainders:
            ret = min(ret, i - remainders[pair])
        remainders[prefix_sum] = i
    return -1 if ret == float('inf') else ret


nums = [3, 1, 4, 2]
p = 6
print(minSubarray(nums, p))  # 1

nums = [6, 3, 5, 2]
p = 9
print(minSubarray(nums, p))  # 2

nums = [1, 2, 3]
p = 3
print(minSubarray(nums, p))  # 0
