from typing import List

def longestSubarray(nums: List[int]) -> int:
    cummulates = [0]
    for i in range(len(nums)):
        if nums[i] == 1:
            cummulates[-1] += 1
        else:
            cummulates.append(0)
    
    if len(cummulates) == 1:
        return cummulates[0]-1
    
    res = 0
    for i in range(1, len(cummulates)):
        res = max(res, cummulates[i] + cummulates[i-1])
    return res


nums = [1,1,0,1]
print(longestSubarray(nums))
# Output: 3

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))
# Output: 5