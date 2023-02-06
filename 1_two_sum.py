from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    remains = {}
    for i, num in enumerate(nums):
        if num in remains:
            return [i, remains[num]]
        remains[target-num] = i


nums = [2,7,11,15]
target = 9 
print(twoSum(nums, target)) # Output: [0,1]

nums = [3,2,4]
target = 6 # [1,2]
print(twoSum(nums, target))

nums = [3,3]
target = 6 # [0,1]
print(twoSum(nums, target))
