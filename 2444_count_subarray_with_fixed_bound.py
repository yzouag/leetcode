from typing import List
def countSubarrays(nums: List[int], minK: int, maxK: int) -> int:
    minPos = -1
    maxPos = -1
    leftBound = -1
    result = 0
    # let i be the number of subarrays end with index i
    # [7, 1, 2, 3, 1, 5, 4] minK = 1, maxK = 5, i = 6
    #  |           |  |  |
    # leftBound  min max i
    # keep track of the most recent min and most recent max
    # the valid subarray (includes i) are all arrays from [1,2,3,1,5,4] to [1,5,4], in total min(min, max) - leftBound
    # for another case:
    # [1,3,5,2,7,5] minK = 1, maxK = 5, i = 5
    #  |       | |
    # min  leftBound i,max
    # when i = 4, update the leftBound since its out of range, now leftBound > min(min, max), no valid subarray in this case
    for i, num in enumerate(nums):
        if num > maxK or num < minK:
            leftBound = i
        if num == minK:
            minPos = i
        if num == maxK:
            maxPos = i
        if leftBound < min(minPos, maxPos):
            result += min(minPos, maxPos) - leftBound
    return result

nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
print(countSubarrays(nums, minK, maxK))
# Output: 2

nums = [1,1,1,1]
minK = 1
maxK = 1
print(countSubarrays(nums, minK, maxK))
# Output: 10