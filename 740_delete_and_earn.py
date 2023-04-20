from typing import List
from collections import Counter

def deleteAndEarn(nums: List[int]) -> int:
    c = Counter(nums)

    nums_list = sorted(c.keys())
    n = len(nums_list)
    nums_list.insert(0, -1)

    take = [0] * (n+1)
    skip = [0] * (n+1)
    res = 0
    for i in range(1, n+1):
        if nums_list[i] - nums_list[i-1] > 1:
            take[i] = max(take[i-1], skip[i-1]) + nums_list[i] * c[nums_list[i]]
        else:
            take[i] = skip[i-1] + nums_list[i] * c[nums_list[i]]
        skip[i] = max(take[i-1], skip[i-1])
        res = max(take[i], skip[i])

    return res

nums = [3,4,2]
print(deleteAndEarn(nums))
# Output: 6

nums = [2,2,3,3,3,4]
print(deleteAndEarn(nums))
# Output: 9

nums = [1,1,1,2,4,5,5,5,6]
print(deleteAndEarn(nums))
# Output: 18

nums = [1,6,3,3,8,4,8,10,1,3]
print(deleteAndEarn(nums))
# Output: 43