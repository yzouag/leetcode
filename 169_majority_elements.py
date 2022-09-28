from typing import List

def majorityElement(nums: List[int]) -> int:
    majority_num = nums[0]
    majority_count = 1
    for i in range(1, len(nums)):
        if majority_count == 0:
            majority_num = nums[i]
            majority_count = 1
            continue

        if nums[i] == majority_num:
            majority_count += 1
        else:
            majority_count -= 1
    return majority_num


nums = [3,2,3]
print(majorityElement(nums))
# Output: 3

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
# Output: 2