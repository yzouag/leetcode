from typing import List
def increasingTriplet(nums: List[int]) -> bool:
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

nums = [1,2,3,4,5]
print(increasingTriplet(nums))
# Output: true

nums = [5,4,3,2,1]
print(increasingTriplet(nums))
# Output: false

nums = [2,1,5,0,4,6]
print(increasingTriplet(nums))
# Output: true