from typing import List
def removeDuplicates(nums: List[int]) -> int:
    curr_num, curr_valid, curr_counts = nums[0], 1, 1
    for num in nums[1:]:
        if curr_num == num:
            if curr_counts == 1:
                curr_counts += 1
                nums[curr_valid] = num
                curr_valid += 1
        else:
            curr_num = num
            curr_counts = 1
            nums[curr_valid] = num
            curr_valid += 1
    return curr_valid

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))
print(nums)
# Output: 5, nums = [1,1,2,2,3,_]

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
print(nums)
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]