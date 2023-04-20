from typing import List
from collections import defaultdict

def longestSubsequence(arr: List[int], difference: int) -> int:
    arr_index_dict = defaultdict(list)
    for i, num in enumerate(arr):
        arr_index_dict[num].append(i)
    
    dp = [1] * len(arr)
    res = 0
    for i in range(1, len(arr)):
        for j in arr_index_dict[arr[i]-difference]:
            if j < i:
                dp[i] = max(dp[i], dp[j]+1)
        res = max(res, dp[i])
    return res

arr = [1,2,3,4]
difference = 1
print(longestSubsequence(arr, difference))
# Output: 4

arr = [1,3,5,7]
difference = 1
print(longestSubsequence(arr, difference))
# Output: 1

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(longestSubsequence(arr, difference))
# Output: 4

arr = [6,-2,0,3,-7,6,-5,-8]
difference = -5
print(longestSubsequence(arr, difference))
# Output: 2