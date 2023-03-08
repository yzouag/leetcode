from typing import List

# here review the merge sort
def sortArray(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])
    i, j = 0, 0
    res = []
    while True:
        if i == len(left):
            res.extend(right[j:])
            break
        if j == len(right):
            res.extend(left[i:])
            break
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

nums = [5,2,3,1]
print(sortArray(nums))
# Output: [1,2,3,5]

nums = [5,1,1,2,0,0]
print(sortArray(nums))
# Output: [0,0,1,1,2,5]