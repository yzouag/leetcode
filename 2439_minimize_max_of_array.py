from typing import List
from math import ceil

def minimizeArrayValue(nums: List[int]) -> int:
    # n = len(nums)
    # changed = True
    # while changed:
    #     changed = False

    #     max_value = max(nums)
    #     for i in range(1, n):
    #         if nums[i] == max_value:
    #             mid = (nums[i] + nums[i-1])//2
    #             if mid != nums[i]:
    #                 changed = True
    #                 nums[i-1] += nums[i]-mid
    #                 nums[i] = mid
    
    # return max(nums)
    
    # the best result we can get for array[0:current]
    # is the average of this subarray, or the previous array[0:current-1]'s best result
    # whichever is larger
    # if previous is larger, even the new average is lower, we cannot reduce number in previous to move to current
    answer = 0
    prefix_sum = 0
    
    # Iterate over nums, update prefix sum and answer.
    for i in range(len(nums)):
        prefix_sum += nums[i]
        answer = max(answer, ceil(prefix_sum / (i + 1)))

    return answer

nums = [3,7,1,6]
print(minimizeArrayValue(nums))
# Output: 5

nums = [10,1]
print(minimizeArrayValue(nums))
# Output: 10

nums = [13,13,20,0,8,9,9]
print(minimizeArrayValue(nums))
# Output: 16