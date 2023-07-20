from typing import List

def longestArithSeqLength(nums: List[int]) -> int:
    # top down approach failed
    # memory exceeded
    # n = len(nums)
    # memo = {}
    # def dfs(i, diff, prev):
    #     if i >= n:
    #         return 0
    #     if (i, diff, prev) in memo:
    #         return memo[(i, diff, prev)]
    #     res = 0
    #     # include current number
    #     if diff == None:
    #         if prev == None:
    #             res = max(res, 1+dfs(i+1, None, nums[i]))
    #         else:
    #             res = max(res, 1+dfs(i+1, nums[i]-prev, nums[i]))
    #     else:
    #         if nums[i]-prev == diff:
    #             res = max(res, 1+dfs(i+1, diff, nums[i]))

    #     res = max(res, dfs(i+1, diff, prev))
    #     memo[(i, diff, prev)] = res
    #     return res
        
    # return dfs(0, None, None)

    # dp[i, diff] is the length of arithmetic array ends at index i with difference diff
    dp = {}
    for right in range(len(nums)):
        for left in range(0, right):
            dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1   
    
    return max(dp.values())

nums = [3,6,9,12]
print(longestArithSeqLength(nums))
# Output: 4

nums = [9,4,7,2,10]
print(longestArithSeqLength(nums))
# Output: 3

nums = [20,1,15,3,10,5,8]
print(longestArithSeqLength(nums))
# Output: 4

nums = [22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52]
print(longestArithSeqLength(nums))
# Output: 6