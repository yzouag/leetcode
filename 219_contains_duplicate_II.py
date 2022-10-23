from collections import defaultdict
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_freq = defaultdict(int)
    
    start_pointer = end_pointer = 0
    while end_pointer <= k and end_pointer < len(nums):
        num_freq[nums[end_pointer]] += 1
        if num_freq[nums[end_pointer]] > 1:
            return True
        end_pointer += 1
    
    while end_pointer < len(nums):
        num_freq[nums[start_pointer]] -= 1
        start_pointer += 1
        
        num_freq[nums[end_pointer]] += 1
        if num_freq[nums[end_pointer]] > 1:
            return True
        end_pointer += 1
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))
# Output: true

nums = [1,0,1,1]
k = 1
print(containsNearbyDuplicate(nums, k))
# Output: true


nums = [1,2,3,1,2,3]
k = 2
print(containsNearbyDuplicate(nums, k))
# Output: false