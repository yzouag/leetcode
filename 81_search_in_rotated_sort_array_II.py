from typing import List
# the rotated sorted array is like two ascending array concatenated
# and any nums[0] ~ nums[rotateIndex] > nums[-1]
def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right)//2
        # mid could appear in two locations
        if nums[mid] == target:
            return True
        if nums[mid] == nums[right]: # Fail to estimate which side is sorted
            right -= 1  # In worst case: O(n)
            continue
        if nums[mid] >= nums[0]: # mid is in the first part
            if nums[mid] < target or nums[0] > target:
                left = mid + 1
            else:
                right = mid - 1
        else: # mid is in the second part
            if nums[mid] > target or nums[-1] < target:
                right = mid -1
            else:
                left = mid + 1
    return False

nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))
# Output: true

nums = [2,5,6,0,0,1,2]
target = 3
print(search(nums, target))
# Output: false

nums = [3,7,8,9,0,1,2]
target = 1
print(search(nums, target))
# Output: true

nums = [1,0,1,1,1]
target = 0
print(search(nums, target))
# Output: true