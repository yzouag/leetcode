from typing import List
import heapq
def minimumDeviation(nums: List[int]) -> int:
    curr_min = float('inf')
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            nums[i] *= 2
        if nums[i] < curr_min:
            curr_min = nums[i]
        nums[i] = -nums[i]
    heapq.heapify(nums)
    
    min_dev = float('inf')
    while nums[0] % 2 == 0:
        if -nums[0] - curr_min < min_dev:
            min_dev = -nums[0] - curr_min
        num = heapq.heappop(nums)
        num //= 2
        if -num < curr_min:
            curr_min = -num
        heapq.heappush(nums, num)
    if -nums[0] - curr_min < min_dev:
        min_dev = -nums[0] - curr_min
    return min_dev
    


nums = [1,2,3,4]
print(minimumDeviation(nums))
# Output: 1

nums = [4,1,5,20,3]
print(minimumDeviation(nums))
# Output: 3

nums = [2,10,8]
print(minimumDeviation(nums))
# Output: 3