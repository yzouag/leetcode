from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort()
    longest = temp = 1
    for i in range(1, len(nums)):
        if nums[i] == (nums[i-1] + 1):
            temp += 1
        else:
            longest = max(longest, temp)
            temp = 1
    longest = max(longest, temp)
    return longest
            

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
# Output: 4

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))
# Output: 9