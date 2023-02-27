from typing import List
def singleNonDuplicate(nums: List[int]) -> int:
    N = len(nums)
    l, r = 0, N-1
    while l < r:
        mid = (l+r) // 2
        if (nums[mid] == nums[mid-1] and (N+1)%4==0) or (nums[mid] == nums[mid+1] and (N+1)%4!=0):
            l = mid
            continue
        if (nums[mid] == nums[mid-1] and (N+1)%4!=0) or (nums[mid] == nums[mid+1] and (N+1)%4==0):
            r = mid
            continue
        return nums[mid]

nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))
# Output: 2

nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))
# Output: 10