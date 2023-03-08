from typing import List
from collections import defaultdict
def findTargetSumWays(nums: List[int], target: int) -> int:
    # seen = {}

    # def dp(nums, target):
    #     if len(nums) == 1:
    #         if abs(nums[0]) == abs(target):
    #             if nums[0] == 0:
    #                 return 2
    #             else:
    #                 return 1
    #         else:
    #             return 0
    #     if (len(nums)-1, target+nums[-1]) in seen:
    #         plus = seen[(len(nums)-1, target+nums[-1])]
    #     else:
    #         plus = dp(nums[:-1], target+nums[-1])
    #         seen[(len(nums)-1, target+nums[-1])] = plus

    #     if (len(nums)-1, target-nums[-1]) in seen:
    #         minus = seen[(len(nums)-1, target-nums[-1])]
    #     else:
    #         minus = dp(nums[:-1], target-nums[-1])
    #         seen[(len(nums)-1, target-nums[-1])] = minus

    #     return plus + minus

    # return dp(nums, target)

    previous_counts = defaultdict(int)
    previous_counts[0] = 1
    for num in nums:
        temp = defaultdict(int)
        for k in previous_counts:
            temp[k+num] += previous_counts[k]
            temp[k-num] += previous_counts[k]
        previous_counts = temp
    return previous_counts[target]


nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))
# Output: 5

nums = [1]
target = 1
print(findTargetSumWays(nums, target))
# Output: 1