from typing import List

# 1. use prefix sum, prefix_sum[i] - prefix_sum[j] is sum(nums[j+1, i+1])
# 2. dividible by k, then prefix_sum[i], prefix_sum[j] should have same remainder when mod k
# 3. we need to keep track of all the results of prefix_sum[i] % k

def subarraysDivByK(nums: List[int], k: int) -> int:
    N = len(nums)
    remainders = {i:0 for i in range(k)}
    prefix_sum = 0
    for i in range(N):
        prefix_sum = (nums[i] + prefix_sum) % k
        remainders[prefix_sum] += 1
    res = 0
    for k in remainders:
        if k == 0: # for this case, the array itself can divided by k
            res += remainders[k]
        res += remainders[k] * (remainders[k] - 1) // 2 # C(n, 2) = n*(n-1)/2
    return res


nums = [4,5,0,-2,-3,1]
k = 7
print(subarraysDivByK(nums, k)) # 5

nums = [5]
k = 9
print(subarraysDivByK(nums, k)) # 0