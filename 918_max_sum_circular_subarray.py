from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    # two cases:
    # 1. the subarray is within the normal array [1, 2, {3, 4}, 5]
    #    in this case, just the normal dp method
    # 2. the subarray is by circular  [1}, 2, 3, {4, 5]
    #    we can transform this question to be, finding the minimum of subarray in normal array
    #    the answer is just the total sum of array minus this minimum (as long as the minimum is negative)
    # 3. one corner case is all number is negative, in this case 2 will return sum of total array
    #    and 1 will return the largest element in the array, in this case 1 is the correct answer

    # denote dp[i] as the min/max of subarray included nums[i]
    # dp[i] = max(nums[i], dp[i-1]+nums[i])  get max subarray
    # dp[i] = min(nums[i], dp[i-1]+nums[i])  get min subarray

    total_sum = sum(nums)
    # maximum = float('-inf')
    # minimum = float('inf')

    maximum = minimum = dp_min = dp_max = nums[0]
    for i in range(1, len(nums)):
        dp_max = max(nums[i], dp_max+nums[i])
        maximum = max(maximum, dp_max)
        dp_min = min(nums[i], dp_min+nums[i])
        minimum = min(minimum, dp_min)
    
    if total_sum == minimum:
        return maximum
    return max(maximum, total_sum - minimum)
    

nums = [1,-2,3,-2]
print(maxSubarraySumCircular(nums)) # 3

nums = [5,-3,5]
print(maxSubarraySumCircular(nums)) # 10

nums = [-3,-2,-3]
print(maxSubarraySumCircular(nums)) # -2