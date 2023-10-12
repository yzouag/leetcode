from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    sums = sum(nums[:k])
    max_sums = sums
    for i in range(k, len(nums)):
        sums -= nums[i-k]
        sums += nums[i]
        max_sums = max(max_sums, sums)
    return max_sums/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))
# Output: 12.75000

nums = [5]
k = 1
print(findMaxAverage(nums, k))
# Output: 5.00000