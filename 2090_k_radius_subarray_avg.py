from typing import List
from math import trunc

def getAverages(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = [-1] * n
    
    if n < 2*k+1:
        return res
    
    sums = sum(nums[:2*k+1])
    res[k] = sums

    for i in range(n):
        if i <= k or i+k >= n:
            continue
        sums -= nums[i-k-1]
        sums += nums[i+k]
        res[i] = sums
    
    for i in range(n):
        if res[i] != -1:
            res[i] = trunc(res[i]/(2*k+1))

    return res


nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(getAverages(nums, k))
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]

nums = [100000]
k = 0
print(getAverages(nums, k))
# Output: [100000]

nums = [8]
k = 100000
print(getAverages(nums, k))
# Output: [-1]