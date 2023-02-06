from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res


nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))
# Output: [2,3,5,4,1,7] 

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))
# Output: [1,4,2,3,3,2,4,1]

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))
# Output: [1,2,1,2]