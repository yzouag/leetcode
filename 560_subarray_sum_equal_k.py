from collections import defaultdict
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    # method 1: brutal force, TLE
    # count = 0
    # new_array = nums.copy()
    # for i in range(1, len(nums)+1):
    #     for j in range(len(new_array)-i+1):
    #         if new_array[j] == k:
    #             count += 1
    #     for j in range(len(new_array)-i):
    #         new_array[j] = new_array[j] + nums[j+i]
    # return count

    # prefix sum
    # we first compute a prefix sum for this array
    # say array is [1 2 3 4 5] k=9
    # the prefix sum, is the sum of array to i th index
    # which is pre = [1 3 6 10 15]
    # now if we what to find a subarray i j, it is pre[j]-pre[i]
    # then the qualified subarray is pre[j]-pre[i] == k
    # or, pre[j] - k == pre[i], we need to count how many pre[i] (i < j) that equals pre[j]-k
    # so we use a dictionary, with key (num) : value (counts of this value)
    
    pre = 0 # here we don't need an array for prefix, just accumulate them one by one
    count = 0
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1
    for i in range(len(nums)):
        pre += nums[i] # get the current prefix sum pre[i]
        count += prefix_sum_count[pre-k] # get the number of previous prefix that the value is pre[i]-k
        prefix_sum_count[pre] += 1 # then add the current prefix sum to the dictionary for later prefix to check
    return count

nums = [1,1,1]
k = 2
print(subarraySum(nums, k))
# Output: 2

nums = [1,2,3]
k = 3
print(subarraySum(nums, k))
# Output: 2
