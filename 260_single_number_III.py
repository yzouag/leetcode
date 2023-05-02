from typing import List
def singleNumber(nums: List[int]) -> List[int]:
    res = set()
    for num in nums:
        if num in res:
            res.discard(num)
        else:
            res.add(num)
    return list(res)

nums = [1,2,1,3,2,5]
print(singleNumber(nums))
# Output: [3,5]

nums = [-1,0]
print(singleNumber(nums))
# Output: [-1,0]

nums = [0,1]
print(singleNumber(nums))
# Output: [1,0]