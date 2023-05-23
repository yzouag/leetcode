from typing import List
from math import gcd

# key technique:
# bit-masking
def maxScore(nums: List[int]) -> int:
    memo = {}
    n = len(nums)
    def backtracking(mask, num_ops):
        if mask == 2**n-1: # all selected
            return 0
        if mask in memo:
            return memo[mask]
        
        max_score = 0
        for i in range(n):
            for j in range(i+1, n):
                if (mask >> i) & 1 == 0 and (mask >> j) & 1 == 0: # both empty
                    new_mask = mask | (1 << i) | (1 << j) # mark as selected
                    max_score = max(max_score, num_ops*gcd(nums[i], nums[j]) + backtracking(new_mask, num_ops+1))
        memo[mask] = max_score
        return max_score
        
    return backtracking(0, 1)

nums = [1,2]
print(maxScore(nums))
# Output: 1

nums = [3,4,6,8]
print(maxScore(nums))
# Output: 11

nums = [1,2,3,4,5,6]
print(maxScore(nums))
# Output: 14